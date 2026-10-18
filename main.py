import cv2

img = cv2.imread("images/gsd.png")

cv2.imshow("gsd",img)
btn = cv2.waitKey(0)
while True:


    if btn == ord("e"):

        break

    elif btn == ord("s"):

        cv2.imwrite("./saved images/gsd.png",img)

        break

    elif btn == ord("r"):
        cv2.destroyAllWindows()

        h = int(input("enter height: "))
        w = int(input("enter width: "))

        imgf = cv2.resize(img, (w, h))

        cv2.imshow("gsd_f",imgf)
        btn1 = cv2.waitKey(0)

        if btn1 == ord("s"):
            cv2.imwrite("./saved images/gsd.png",imgf)

            break

        elif btn1 == ord("d"):
            cv2.imwrite("./delete/gsd.png",imgf)

            break
        elif btn1==ord("e"):

            break
