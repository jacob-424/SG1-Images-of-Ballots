import tkinter as tk

""" Programming language & IDE: Python with Thonny

    Team members: Klara Malaj, Ricky Belle, Laura Sobel, Chao Ling, and Jacob Wiley
    
    Date started: 10/07/26
    
    Major revision dates: 10/07/26
                          10/10/26
                          10/11/26
                          10/15/26
                          10/16/26
                          
    Class: Introduction to the Software Profession
    
    Class number: CS 4500-001
    
    Program description: This program takes a specified text file containting only binary digits and converts
    it into an image. This text file should have the same number of binary digits on each line, have at least
    10 lines, and each line should contain at least 20 binary digits. The file is then converted into a PNG
    where each '0' corresponds to a black pixel and '1' corresponds to a white pixel. This image will be
    displayed in a new window and saved to the program directory as IMAGE1.png.
             
    A second user supplied file, IMAGE2.png, is taken from program directory and then displayed. From
    IMAGE2.png, a new image file is created named IMAGE3.png. This file is also displayed and saved to the
    program directory. IMAGE3.png will be a copy of IMAGE2.png but with all instances of the following pattern
    highlighted red:
             
            11111011111
            11111011111
            11111011111
            11111011111
            11111011111
            00000000000
            11111011111
            11111011111
            11111011111
            11111011111
            11111011111
             
    The coordinates of any found occurrence of this pattern in IMAGE2.png will also be displayed.
    
    External files used:
        Text file: A user supplied text file containing only binary digits
        IMAGE2.png: A user supplied image file containing only black and white pixels
"""

def getTextFileName():
    """ Prompts the user for the name of the binary text file.
        Created by ChatGPT.
        
    Returns:
        filename (string): File name ending in ".txt"
    """
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
        binary (string): Contents of the user supplied text file located in the project directory.
        
    Returns:
        True: binary is a valid binary file.

    Raises:
        ValueError: binary is an invalid binary file.
        
    Sources:
        For learning splitlines(): https://www.geeksforgeeks.org/python/python-string-splitlines-method/
        For learning lists more:  https://www.geeksforgeeks.org/python/python-lists/
    """
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
        True: Conversion and file output succeeded.
        False: Failed to save IMAGE1.png.
    
    Outputs:
        IMAGE1.png: binary converted to an image.

    Sources:
        For handling and display PNGs: https://docs.python.org/3/library/tkinter.html#
        For learning enumerate(): https://www.geeksforgeeks.org/python/access-the-index-and-value-using-python-for-loop/
    """
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
                
    # Attempt to save img as IMAGE1.png
    try:
        img.write(filename="IMAGE1.png")
    except tk.TclError as e:
        print(f"Failed to save image: {e}")
        return False
    
    return True
                
def image2ToMatrix():
    """ Converts IMAGE2.PNG into a matrix of 0's and 1's.
        
    Returns:
        zerosAndOnes (matrix): IMAGE2.png converted into a matrix.
    
    Sources:
        https://docs.python.org/3/library/tkinter.html
    """
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
    
    Sources:
        https://docs.python.org/3/tutorial/controlflow.html
    """
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
    
    Returns:
        True: Conversion and file output succeeded
        False: Failed to save IMAGE3.png
        
    Outputs:
        IMAGE3.png: zerosAndOnes converted to an image with each plus highlighted red.
    """
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

    # Attempt to save img as IMAGE3.png
    try:
        img.write(filename="IMAGE3.png") # Overwrites an existing file
    except tk.TclError as e:
        print(f"Failed to save image: {e}")
        return False
    
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
    print("""Program description: This program takes a specified text file containting only binary digits and converts
it into an image. This text file should have the same number of binary digits on each line, have at least
10 lines, and each line should contain at least 20 binary digits. The file is then converted into a PNG
where each '0' corresponds to a black pixel and '1' corresponds to a white pixel. This image will be
displayed in a new window and saved to the program directory as IMAGE1.png.
             
A second user supplied file, IMAGE2.png, is taken from program directory and then displayed. From
IMAGE2.png, a new image file is created named IMAGE3.png. This file is also displayed and saved to the
program directory. IMAGE3.png will be a copy of IMAGE2.png but with all instances of the following pattern
highlighted red:
             
        11111011111
        11111011111
        11111011111
        11111011111
        11111011111
        00000000000
        11111011111
        11111011111
        11111011111
        11111011111
        11111011111
             
The coordinates of any found occurrence of this pattern in IMAGE2.png will also be displayed.""")
    print()
    
    ### IMAGE1.png
    
    root = tk.Tk() # Initialize tkinter
    root.withdraw() # Hide main window
        
    # Get the file name from the user
    filename = getTextFileName()

    # Attempt to open the file.
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
    
    # Check that the file is valid. If it's valid, output its contents.
    try:
        if validateBinary(binary):
            print(filename + ":\n")
            print(binary)
    except ValueError as e:
        print("Error: " + str(e))
        input("Press ENTER to exit.\n")
        return
    
    # Convert the file to IMAGE1.png and output it
    # Note: The displayed window must be closed before the program can continue
    if binaryToImage1(binary):
        displayImage("IMAGE1.png", root)
        
    ### IMAGE2.png
    
    # Display IMAGE2.png.
    displayImage("IMAGE2.PNG", root)
    
    # Convert IMAGE2 into zerosAndOnes.
    zerosAndOnes = image2ToMatrix()

    # Get the coordinates of each occurrence of the plus pattern.
    coords = searchForPattern(zerosAndOnes)

    # Output how many were found and where.
    print("Number of patterns found:", len(coords))
    print("Pattern center coordinates (row, column):", coords)
    
    ### IMAGE3.png

    # Convert the matrix to IMAGE3.png
    if matrixToImage3(zerosAndOnes, coords):
        displayImage("IMAGE3.png", root)

    # Wait for the user to press ENTER before ending
    input("Press ENTER to exit.\n")
    
if __name__ == "__main__":
    main()