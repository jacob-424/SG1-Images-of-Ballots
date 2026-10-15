import tkinter as tk

#TODO: Add opening comment

def getTextFileName():
    """ Prompts the user for the name of the binary text file.
        Created by ChatGPT.
        
    Returns:
        filename (string): File name ending in ".txt"
    """
    # From project reqs: "The function GetTextFileName should prompt the user for the name of a file. The file name should finish
    # with “.TXT”. (The case of the letters in “txt” should not matter, and there shouldn’t be quote marks.)
    # If the filename does NOT end in “.txt”, GetTextFileName should give a descriptive error message and reprompt.
    # If the user enters a null string,  GetTextFileName should give a descriptive error message and reprompt. If
    # your group thinks of other things the user might do wrong when entering a Windows 11 filename, your
    # GetTextFileName should protect against those problems as well, again using a precise descriptive error
    # message before reprompting. When the user has supplied a name that follows the rules for a Windows 11 file
    # name the ends in .txt, GetTextFileName should return that filename as a string to the caller."
    
    while True:
        filename = input("Enter the name of a text file: ")

        if filename == "":
            print("Error: The filename cannot be empty.")
            continue

        if not filename.lower().endswith(".txt"):
            print("Error: The filename must end with .txt.")
            continue

        invalid_characters = '<>:"/\\|?*'

        if any(character in filename for character in invalid_characters):
            print("Error: The filename contains characters that are not allowed in Windows filenames.")
            continue

        if filename.endswith(" ") or filename.endswith("."):
            print("Error: A Windows filename cannot end with a space or period.")
            continue

        return filename
    
def validateBinary(binary):
    """ Checks that binary contains only 0's and 1's, has the same amount of digits on each line, has at least 10 lines, and
        that each line contains at least 20 digits.
    
    Args:
        binary (string): Contents of the user supplied file located in the project directory.
        
    Returns:
        True: binary is a valid binary file.

    Raises:
        ValueError: binary is an invalid binary file.
        
    Sources:
        For learning splitlines(): https://www.geeksforgeeks.org/python/python-string-splitlines-method/
        For learning lists more:  https://www.geeksforgeeks.org/python/python-lists/
    """
    # From project reqs: "SG1 should make sure that the text file includes only text lines of zeroes
    # and ones. If the file includes anything else, SG1 should give an appropriate error message, prompt
    # for an ENTER, and halt when ENTER is pressed. (The text file will also contain end-of-line and end-of-file
    # markers, but otherwise it should only have 0’s and 1’s.) There should also be the same number of binary
    # characters on each line. There should be at least 10 lines, and each line should contain at least 20
    # characters. If not, SG1 should give an appropriate error message and halt on an ENTER, as above."
    
    lines = binary.splitlines()
    
    # Checks if the file was empty
    if len(lines) == 0:
        raise ValueError("Each file line must contain at least 20 binary digits.")
        
    length = len(lines[0]) # For checking that each line is the same length
    
    if len(lines) < 10:
        raise ValueError("File must contain at least 10 lines.")
    
    for line in lines:
        if len(line) != length:
            raise ValueError("Each file line must have the same length.")
        
        if len(line) < 20:
            raise ValueError("Each file line must contain at least 20 binary digits.")
        
        for char in line:
            if  char != '0' and char != '1':
                raise ValueError("File must only contain binary digits.")
    
    return True
    
def binaryToImage1(binary):
    """ Converts binary into a black and white image where 0's are black pixels and 1's are white pixels.
        The image will be named IMAGE1.png, saved in the project directory, and output to the screen.
    Args:
        binary (string): The binary file contents to be converted to IMAGE1.png.
        
    Returns:
        True: Conversion and file output succeeded
    
    Outputs:
        IMAGE1.png: binary converted to an image.

    Sources:
        For handling and display PNGs: https://docs.python.org/3/library/tkinter.html#
        For learning enumerate(): https://www.geeksforgeeks.org/python/access-the-index-and-value-using-python-for-loop/
    """
    # From project reqs: "Then SG1 should convert the binary file into a .PNG black and white image file where a 0 will
    # correspond to a black pixel, and a 1 will correspond to a white pixel. The first line of text should convert to the highest
    # row of pixels, the last line of text should correspond to the bottom line of pixels. The following illustration is too small
    # for a legal SG1 input file, but I hope it helps get the point across. Note that the top row is all white, so appears blank on
    # the page."
    # Note: The actual project requirements has the example image of what it should look like.
    #
    # "Once you have converted the text file of binary digits into a black and white .PNG image file, display resulting
    # image to the screen, and output it to the current directory with the name IMAGE1.PNG. If there already exists a
    # file with that name in the current directory, overwrite it. If no file with that name exists, make a new file with
    # that name."
    
    lines = binary.splitlines()
    num_of_cols = len(lines[0])
    num_of_rows = len(lines)
    
    img = tk.PhotoImage(width=num_of_cols, height=num_of_rows)
    
    # Create pixels
    for y, line in enumerate(lines):
        for x, bit in enumerate(line):
            if bit == '0':
                img.put(data="black", to=(x, y))
            elif bit == '1':
                img.put(data="white", to=(x, y))
                
    #img = img.zoom(5) # Magnify the image by a factor of 5
    img.write(filename="IMAGE1.png")
    # TODO: Add error check when fail to write while image is open
    return True
                
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

    image = tk.PhotoImage(file="IMAGE2.PNG")

    width = image.width()
    height = image.height()

    zerosAndOnes = []

    # Go through every pixel in IMAGE2
    for row in range(height):
        currentRow = []

        for col in range(width):
            pixel = image.get(col, row)

            # Black pixel = 0, anything else = 1
            if pixel == (0, 0, 0):
                currentRow.append(0)
            else:
                currentRow.append(1)

        zerosAndOnes.append(currentRow)

    return zerosAndOnes
    
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

    pattern = [
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    ]

    coords = []

    rows = len(zerosAndOnes)
    cols = len(zerosAndOnes[0])

    # Try every possible location where an 11x11 pattern can fit
    for row in range(rows - 10):
        for col in range(cols - 10):

            match = True

            # Compare the 11x11 area with the required pattern
            for patternRow in range(11):
                for patternCol in range(11):
                    if zerosAndOnes[row + patternRow][col + patternCol] != pattern[patternRow][patternCol]:
                        match = False
                        break

                if not match:
                    break

            # Save the center of the pattern
            if match:
                coords.append((row + 5, col + 5))

    return coords

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

    PLUS_RADIUS = 5  # The pattern is 11x11, so 5 pixels on each side of the middle

    num_of_rows = len(zerosAndOnes)
    num_of_cols = len(zerosAndOnes[0])

    img = tk.PhotoImage(width=num_of_cols, height=num_of_rows)

    # Start with the black and white image (0 = black, 1 = white)
    for y in range(num_of_rows):
        for x in range(num_of_cols):
            if zerosAndOnes[y][x] == 0:
                img.put(data="black", to=(x, y))
            else:
                img.put(data="white", to=(x, y))

    # For each plus found, turn the white background pixels inside its 11x11 area red.
    # The black plus itself is left alone.
    for (row, col) in coords:
        for y in range(row - PLUS_RADIUS, row + PLUS_RADIUS + 1):
            for x in range(col - PLUS_RADIUS, col + PLUS_RADIUS + 1):
                if 0 <= y < num_of_rows and 0 <= x < num_of_cols and zerosAndOnes[y][x] == 1:
                    img.put(data='red', to=(x, y))

    img.write(filename="IMAGE3.png")  # Overwrites an existing file
    return True


def displayImage(img_filename, root):
    """ Displays img_filename in a new window. Program flow will not continue until this window is closed.

    Args:
        img_filename (string): The file name of the image to be displayed.
        root (tkinter): The main tkinter object.
        
    Sources:
        For displaying images: https://docs.python.org/3/library/tkinter.html#
    """    
    window = tk.Toplevel(root) # Create window containter
    window.title(img_filename + " - Close to continue program")
    window.minsize(640, 360)
    window.attributes("-topmost", True)
    
    img = tk.PhotoImage(file=img_filename) # Get IMAGE1
    img = img.zoom(3) # Magnify the image
    
    label = tk.Label(window, image=img) # Put IMAGE1 inside the label
    label.pack() # Pack the label inside window
    
    root.wait_window(window) # Display and wait until window is closed
    
    
def main():
    # TODO: From project reqs: "write to the screen a short (one screen or less) explanation of what the program does."
    
    ### IMAGE1.png
    
    root = tk.Tk() # Initialize tkinter
    root.withdraw() # Hide main window
        
    # Get the file name from the user using getTextFileName().
    filename = getTextFileName()

    # Attempt to open the file.
    # From project reqs: "Once the user has supplied a legitimate text file name, SG1 should attempt
    # to open that file in the same directory where the program is running. If no file with that name
    # exists in the current directory, a descriptive error message should be printed to the screen,
    # and the user should be prompted to push ENTER. When the user pushes ENTER, SG1 should stop.
    # If the user correctly enters a text file name that does exist in the current directory, then SG1
    # should open the file."
    try:
        file = open(filename, "r", encoding="utf-8")
        binary = file.read()
        file.close()
    except FileNotFoundError:
        print("Error: File does not exist.")
        input("Press ENTER to exit.\n")
        return
    except Exception as e:
        print("Error: File could not be read.")
        print("System Output: " + str(e))
        input("Press ENTER to exit.\n")
        file.close()
        return
    
    # Check that the file is valid using validateBinary(). If it's valid, output its contents.
    try:
        if validateBinary(binary):
            print(filename + ":\n")
            print(binary)
    except ValueError as e:
        print("Error: " + str(e))
        input("Press ENTER to exit.\n")
        return
    
    # Convert the file to IMAGE1.png using binaryToImage1() and output it
    # Note: The displayed window must be closed before the program can continue
    if binaryToImage1(binary):
        displayImage("IMAGE1.png", root)
        
    ### IMAGE2.png
    
    # Display IMAGE2.png.
    displayImage("IMAGE2.PNG", root)

    
    # Convert IMAGE2 into zerosAndOnes using image2ToMatrix().
    zerosAndOnes = image2ToMatrix()

    
    # Get the coordinates of each occurrence of the plus pattern using searchForPattern(). 
    coords = searchForPattern(zerosAndOnes)


    # Output how many were found and where.
    print("Number of patterns found:", len(coords))
    print("Pattern center coordinates (row, column):", coords)
    
    ### IMAGE3.png
    
    # TODO: Convert zerosAndOnes to IMAGE3.png with matrixToImage3().
    #       Display IMAGE3.png.
    
    # TODO: From project reqs: "Then SG1 should instruct the user to push ENTER to end the program. When the user
    #       pushes ENTER, SG1 should halt."
    
if __name__ == "__main__":
    main()