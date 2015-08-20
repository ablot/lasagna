
"""
Read MHD stacks (using the vtk library) or TIFF stacks
@author: Rob Campbell - Basel - git<a>raacampbell.com
https://github.com/raacampbell13/lasagna
"""


from __future__ import division
import re
import os
import struct 
import numpy as np
import imp #to look for the presence of a module. Python 3 will require importlib
import lasagna_helperFunctions as lasHelp 

def loadTiffStack(fname):
  """
  Read a TIFF stack.
  Bugs: known to fail with tiffs produced by Icy [23/07/15]

  """
  #I think TIFF3D uses libtiff whereas TIFFfile is pure python. Provide both options
  purePython = True
  if purePython:
    from libtiff import TIFF3D
    tiff3d = TIFF3D.open(fname)
    print "Loading:\n" + tiff3d.info() + "\n"
    im = tiff3d.read_image()
    tiff3d.close()
  else:
    from libtiff import TIFFfile
    import numpy as np
    tiff = TIFFfile(fname)
    samples, sample_names = tiff.get_samples() #we should have just one
    print "Loading:\n" + tiff.get_info() + "\n"
    im = np.asarray(samples[0])

  print "read image of size: rows: %d, cols: %d, layers: %d" % (im.shape[1],im.shape[2],im.shape[0])
  return im


def mhdRead(fname,fallBackMode = False):
  """
  Read an MHD file using either VTK (if available) or the slower-built in reader
  if fallBackMode is true we force use of the built-in reader
  """

  if fallBackMode == False: 
    #Attempt to load vtk
    try:
      imp.find_module('vtk')
      import vtk
      from vtk.util.numpy_support import vtk_to_numpy
    except ImportError:
      print "Failed to find VTK. Falling back to built in (but slower) MHD reader"
      fallBackMode = True



  if fallBackMode:
    return mhd_read_fallback(fname)
  else:
    #use VTK
    imr = vtk.vtkMetaImageReader()
    imr.SetFileName(fname)
    imr.Update()

    im = imr.GetOutput()
    rows, cols, z = im.GetDimensions()
    sc = im.GetPointData().GetScalars()
    a = vtk_to_numpy(sc)
    print "Using VTK to read MHD image of size: rows: %d, cols: %d, layers: %d" % (rows,cols,z)
    return a.reshape(z, cols, rows) #TODO: Inverted from example I found. Why? Did I fuck up?


def mhd_read_fallback(fname):
  """
  Read the header file from the MHA file then use this to 
  build a 3D stack from the raw file

  fname should be the name of the mhd (header) file
  """

  if os.path.exists(fname) == False:
    print "mha_read can not find file %s" % fname
    return False
  else:
    info = mhd_read_header_file(fname)
    if len(info)==0:
      print "No data extracted from header file"
      return False


  if info.has_key('dimsize') == False:
    print "Can not find dimension size information in MHD file. Not importing data"
    return False


  #read the raw file
  if info.has_key('elementdatafile') == False:
    print "Can not find the data file as the key 'elementdatafile' does not exist in the MHD file"
    return False

  return mhd_read_raw_file(info)


def mhd_read_raw_file(header):
  """
  Raw .raw file associated with the MHD header file
  CAUTION: this may not adhere to MHD specs! Report bugs to author.
  """

  if header.has_key('headersize'):
    if header['headersize']>0:
      print "\n\n **MHD reader can not currently cope with header information in .raw file. Contact the author** \n\n"
      return False

  #Set the endian type correctly
  if header.has_key('byteorder'):
    if header['byteorder'].lower == 'true' :
      endian = '>' #big endian
    else:
      endian = '<' #little endian
  else:
    endian = '<' #little endian


  #Set the data type correctly 
  if header.has_key('datatype'):
    datatype = header['datatype'].lower()

    if datatype == 'float':
      formatType = 'f'
    elif datatype == 'double':
      formatType = 'd'
    elif datatype == 'long':
      formatType = 'l'
    elif datatype == 'ulong':
      formatType = 'L'
    elif datatype == 'char':
      formatType = 'c'
    elif datatype == 'uchar':
      formatType = 'B'
    elif datatype == 'short':
      formatType = 'h'      
    elif datatype == 'ushort':
      formatType = 'H'      
    elif datatype == 'int':
      formatType = 'i'      
    elif datatype == 'uint':
      formatType = 'I'
    else:
      formatType = False

  else:
      formatType = False

  if formatType == False:
    print "\nCan not find data format type in MHD file. **CONTACT AUTHOR**\n"
    return False



  rawFname = header['elementdatafile']
  fid = open(rawFname,'rb')
  data = fid.read()
  fid.close()
  
  dimSize = header['dimsize']
  #from: http://stackoverflow.com/questions/26542345/reading-data-from-a-16-bit-unsigned-big-endian-raw-image-file-in-python
  fmt = endian + str(int(np.prod(dimSize))) + formatType
  pix = np.asarray(struct.unpack(fmt, data))
  
  return pix.reshape((dimSize[2],dimSize[1],dimSize[0]))


def mhd_read_header_file(fname):
  """
  Read an MHD plain text header file and return contents as a dictionary
  """
  fid = open(fname,'r')
  mhd_header = dict()
  mhd_header['FileName'] = fname

  contents = fid.read()
  fid.close()

  info = dict() #header data stored here

  for line in contents.split('\n'):
    if len(line)==0:
      continue

    m=re.match('\A(\w+)',line)
    if m == None:
      continue

    key = m.groups()[0].lower() #This is the data key

    #Now we get the data
    m=re.match('\A\w+ *= * (.*) *',line)
    if m == None:
      print "Can not get data for key %s" % key
      continue

    if len(m.groups())>1:
      print "multiple matches found during mhd_read_header_file. skipping " + key
      continue

    #If we're here, we found reasonable data
    data = m.groups()[0] 

    #If there are any characters not associated with a number we treat as a string and add to the dict
    if re.match('.*[^0-9 \.].*',data) != None:
      info[key] = data
      continue

    #Otherwise we have a single number of a list of numbers in space-separated form. 
    #So we return these as a list or a single number. We convert everything to float just in
    #case it's not an integer. 
    data = data.split(' ')
    numbers = []
    for number in data:
      if len(number)>0:
        numbers.append(float(number))

    #If the list has just one number we return an int
    if len(numbers)==1:
      numbers = float(numbers[0])

    info[key] = numbers

  return info






def getVoxelSpacing(fname,fallBackMode=False):
  """
  Attempts to get the voxel spacing in all three dimensions. This allows us to set the axis
  ratios automatically. TODO: Currently this will only work for MHD files, but we may be able 
  to swing something for TIFFs (e.g. by creating Icy-like metadata files)
  """

  if fname.lower().endswith('.mhd'):

    try:
      imp.find_module('vtk')
      import vtk
    except ImportError:
      print "Failed to find VTK. Using default axis length values"
      #TODO: read values from built-in info reader
      return lasHelp.readPreference('defaultAxisRatios') #defaults


    if fallBackMode==False:      
      imr = vtk.vtkMetaImageReader()
      imr.SetFileName(fname)
      imr.Update()
  
      im = imr.GetOutput()
      spacing = im.GetSpacing()

      if len(spacing)==0: 
        return lasHelp.readPreference('defaultAxisRatios') #defaults
    
      #Determine the ratios from the spacing 
      ratios = [1,1,1]
    
      ratios[0] = spacing[0]/spacing[1]
      ratios[1] = spacing[2]/spacing[0]
      ratios[2] = spacing[1]/spacing[2]
      return ratios

  else:
    return lasHelp.readPreference('defaultAxisRatios') #defaults


def loadStack(fname):
  """
  loadStack determines the data type from the file extension determines what data are to be 
  loaded and chooses the approproate function to return the data.
  """
  if fname.lower().endswith('.tif') or fname.lower().endswith('.tiff'):
    return loadTiffStack(fname)
  elif fname.lower().endswith('.mhd'):
    return mhdRead(fname)
  else:
    print fname + " not loaded. data type unknown"

def imageFilter():
  return "Images (*.mhd *.mha *.tiff *.tif)"