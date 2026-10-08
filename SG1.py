#TODO: Add opening comment

def getTextFileName():
    """ Prompts the user for the name of the binary text file.
        Created by ChatGPT.
    
    Args:
    
    Returns:
        fileName (string): File name ending in ".txt"
        
    Globals:
    
    Sources:
    """
    # TODO: From project reqs: "The function GetTextFileName should prompt the user for the name of a file. The file name should finish
    #       with “.TXT”. (The case of the letters in “txt” should not matter, and there shouldn’t be quote marks.)
    #       If the filename does NOT end in “.txt”, GetTextFileName should give a descriptive error message and reprompt.
    #       If the user enters a null string,  GetTextFileName should give a descriptive error message and reprompt. If
    #       your group thinks of other things the user might do wrong when entering a Windows 11 filename, your
    #       GetTextFileName should protect against those problems as well, again using  a precise descriptive error
    #       message before reprompting. When the user has supplied a name that follows the rules for a Windows 11 file
    #       name the ends in .txt, GetTextFileName should return that filename as a string to the caller."
    
def validateBinary(binaryFile):
    """ Checks that binaryFile contains only 0's and 1's, has the same amount on each line, has at least 10 lines, and
        that each line contains at least 20 characters.
    
    Args:
        binaryFile (file): User supplied binary file located in the project directory.
        
    Returns:
        
    Globals:
    
    Sources:
    """
    # TODO: From project reqs: "SG1 should make sure that the text file includes only text lines of zeroes
    #       and ones. If the file includes anything else, SG1 should give an appropriate error message, prompt
    #       for an ENTER, and halt when ENTER is pressed. (The text file will also contain end-of-line and end-of-file
    #       markers, but otherwise it should only have 0’s and 1’s.) There should also be the same number of binary
    #       characters on each line. There should be at least 10 lines, and each line should contain at least 20
    #       characters. If not, SG1 should give an appropriate error message and halt on an ENTER, as above."
    
def binaryToImage1(binaryFile):
    """ Converts binaryFile into a black and white image where 0's are black pixels and 1's are white pixels.
        The image will be named IMAGE1.png, saved in the project directory, and output to the screen.
    Args:
        binaryFile (file): The file to be converted to IMAGE1.png.
        
    Outputs:
        IMAGE1.png: binaryFile converted to an image.
        
    Globals:
    
    Sources:
    """
    # TODO: From project reqs: "Then SG1 should convert the binary file into a .PNG black and white image file where a 0 will
    #       correspond to a black pixel, and a 1 will correspond to a white pixel. The first line of text should convert to the highest
    #       row of pixels, the last line of text should correspond to the bottom line of pixels. The following illustration is too small
    #       for a legal SG1 input file, but I hope it helps get the point across. Note that the top row is all white, so appears blank on
    #       the page."
    #       Note: The actual project requirements has the example image of what it should look like.
    #
    #       "Once you have converted the text file of binary digits into a black and white .PNG image file, display resulting
    #       image to the screen, and output it to the current directory with the name IMAGE1.PNG. If there already exists a
    #       file with that name in the current directory, overwrite it. If no file with that name exists, make a new file with
    #       that name."
    #       Note: We could either output the image from this function or in main right after, whichever is preferred.
    
def image2ToMatrix():
    """ Converts IMAGE2.PNG into a matrix of 0's and 1's.

    Args:
        
    Returns:
        zerosAndOnes (matrix): IMAGE2.png converted into a matrix.
        
    Globals:
    
    Sources:
    """
    
    # TODO: From project reqs: "SG1 should next convert IMAGE2.PNG into an array (or a list of lists – that’s your choice) that
    #       holds 0’s and 1’s. The PNG pixels will probably have 255 and 0 to make white and black pixels respectively. Wherever
    #       a pixel has the value 0, your matrix should have a 0. If a pixel has any value other than 0, your matrix should have
    #       a 1. I will call this array of values ZerosAndOnes."
    
def searchForPattern(zerosAndOnes):
    """ Searches zerosAndOnes for the plus pattern and returns the coordinates of each occurrence.

    Args:
        zerosAndOnes (matrix): A matrix of 0's and 1's.
        
    Returns:
        coords (list of tuples): The locations of each occurrence of the plus pattern in zerosAndOnes.
        
    Globals:
    
    Sources:
    """
    ## TODO: From project reqs: "SG1 should search ZerosAndOnes, looking for the pattern on the next page:
    #
    #        11111011111
    #        11111011111
    #        11111011111
    #        11111011111
    #        11111011111
    #        00000000000
    #        11111011111
    #        11111011111
    #        11111011111
    #        11111011111
    #        11111011111
    #
    #        This pattern may occur 0, 1 or 2 times in ZerosAndOnes. SG1 should report how many times it finds that exact pattern,
    #        and should give the coordinates of the middle of the pattern (where the horizontal and vertical lines of zeros intersect)
    #        for each pattern found."

def matrixToImage3(zerosAndOnes, coords):
    """ Converts zeroesAndOnes to an image with each plus pattern highlighted red. The converted image will be
        named IMAGE3.png and saved to the project directory.

    Args:
        zerosAndOnes (matrix): A matrix of 0's and 1's.
        coords (list of tuples): The locations of each occurrence of the plus pattern in zerosAndOnes.
        
    Outputs:
        IMAGE3.png: zerosAndOnes converted to an image with each plus highlighted red.
        
    Globals:
    
    Sources:
    """
    # TODO: From project reqs: "Finally, your SG1 program should make a new PNG image called IMAGE3.PNG. IMAGE1.PNG and IMAGE2.PNG are
    #       black and white images. IMAGE3.PNG will be a color image. Wherever IMAGE2.PNG had a white pixel, IMAGE3.PNG should have a white pixel.
    #       For most IMAGE2.PNG pixels that have a black pixel, IMAGE3.PNG should also have a black pixel. However, wherever SG1 detected the
    #       pattern shown above (a plus sign of black pixels in a background of white), the white pixels in that pattern in IMAGE2.PNG  (that is,
    #       the background to the black plus sign) should be changed into red pixels in IMAGE3.PNG. IMAGE3.PNG should be saved to the current directory
    #       as an external file, overwriting any such file if it already exists in the current directory."
    
    
def main():
    # TODO: From project reqs: "write to the screen a short (one screen or less) explanation of what the program does."
    
    ### IMAGE1.png
    
    # TODO: Get the file name from the user using getTextFileName().

    # TODO: Attempt to open the file.
    #       From project reqs: "Once the user has supplied a legitimate text file name, SG1 should attempt
    #       to open that file in the same directory where the program is running. If no file with that name
    #       exists in the current directory, a descriptive error message should be printed to the screen,
    #       and the user should be prompted to push ENTER. When the user pushes ENTER, SG1 should stop.
    #       If the user correctly enters a text file name that does exist in the current directory, then SG1
    #       should open the file."
    
    # TODO: Check that the file is valid using validateBinary(). If it is valid, output its contents.
    
    # TODO: Convert the file to IMAGE1.png and output it using binaryToImage1().
    
    ### IMAGE2.png
    
    # TODO: Display IMAGE2.png.
    
    # TODO: Convert IMAGE2 into zerosAndOnes using image2ToMatrix().
    
    # TODO: Get the coordinates of each occurrence of the plus pattern using searchForPattern(). Output how
    #       many were found and where.
    
    ### IMAGE3.png
    
    # TODO: Convert zerosAndOnes to IMAGE3.png with matrixToImage3().
    #       Display IMAGE3.png.
    
    # TODO: From project reqs: "Then SG1 should instruct the user to push ENTER to end the program. When the user
    #       pushes ENTER, SG1 should halt."
    
if __name__ == "__main__":
    main()