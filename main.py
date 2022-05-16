import cv2
import numpy


img = cv2.imread("pusaa.jpg")


def main():
    print("""
       ACTIVITY #5:
       The program should be:
       1. Accept/load colored img. Grayscale should be rejected.
       2. Output a pixel value.
       3. Modify a pixel value.
       4. Set img dimensions. Within boundaries or not.
       5. Set img total pixel count. Higher or lower than the set pixel.
       6. Show the currently loaded image's data type.
       7. exit
       """)
    opt = int(input("Please enter a number: "))
    if opt == 1:
        checkgray()
    elif opt == 2:
        pixelval()
    elif opt == 3:
        modpix()
    elif opt == 4:
        imgdim()
    elif opt == 5:
        pixelcount()
    elif opt == 6:
        imgdata()
    elif opt == 7:
        exit()
    else:
        print("Please try again!!!")
        main()


def checkgray():
    imgLen = len(img.shape)
    if imgLen >= 3:
        cv2.imshow("colored", img)
        cv2.waitKey(0)
        main()
    else:
        print("grayscale")
        main()


def pixelval():
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    color = int(input("BGR selection: [0. BLUE] [1. GREEN] [2. RED]: "))
    print(img.item(x, y, color))
    main()


def modpix():
    x = int(input("for x axis: "))
    y = int(input("for y axis: "))
    print(img[x, y])
    for i in range(0, 3, 1):
        if i == 0:
            print("Please Enter value for blue")
            pixelValue = int(input("Pixel Value: "))
        elif i == 1:
            print("Please Enter value for green")
            pixelValue = int(input("Pixel Value: "))
        elif i == 2:
            print("Please Enter value for red")
            pixelValue = int(input("Pixel Value: "))

        img.itemset((x, y, i), pixelValue)
    print(img[x, y])
    cv2.imshow("colored", img)
    cv2.waitKey(0)
    main()


def imgdim():
    x = 300
    y = 250
    print(img.shape)
    print(f"""
    total pixel in x-axis: {img.shape[0]}
    total pixel in y-axis: {img.shape[1]}
    compared value in x-axis: {x}
    compared value in y-axis: {y}
     """)

    if x <= img.shape[0] and y <= img.shape[1]:
        print("Within boundaries")
    else:
        print("Out of boundaries")
    main()


def pixelcount():
    x = 300
    y = 250
    fixedValue = x * y
    totalPixel = img.shape[0] * img.shape[1]
    print(f"""
    total fixed variable: {fixedValue}
    total image pixels: {totalPixel}
            """)
    if fixedValue > totalPixel:
        print("higher")
    elif fixedValue < totalPixel:
        print("lower")
    else:
        print("equal")
    main()


def imgdata():
    print(f"image data type is: {img.dtype}")
    main()

if __name__ == "__main__":
    main()

