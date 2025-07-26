import sys
import random
from PIL import Image

def main():
  if len(sys.argv) != 4:
    print("python namecrypt <image.jpg> <height> <width> ")
    sys.exit(1)
  
  if checkfile(sys.argv[1]) == False:
    print("file not in format .jpg")
    sys.exit(1)
  
  newsize = (int(sys.argv[2]),int(sys.argv[3]))
  
  choice = input("enter Y or N").upper()
  
  filename = rename(choice)
  imageinput = Image.open(sys.argv[1])
  imageoutput = imageinput.resize(newsize)
  imageoutput.save(filename)
  print(filename + " saved sucessfully")

def namerandom(array):
  randomname = ""
  for i in range(5):
    randomname += random.choice(array)
  return randomname

def rename(choice):
  filename = ""
  if choice == "Y":
    newname = input("enter a name no jpg")
    filename = newname + ".jpg"
  if choice == "N":
    array = ["a","e","u","k","m"]
    filename = namerandom(array) + ".jpg"
    
  return filename
    
def checkfile(file):
  checkformat = False
  check = file[-3:]
  if str(check) == "jpg":
    checkformat = True
  return checkformat

if __name__ == '__main__':
  main()