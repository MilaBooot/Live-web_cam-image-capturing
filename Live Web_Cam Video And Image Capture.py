import cv2, time
        #Creat an object .Zero for an external camera
video=cv2.VideoCapture(0)
a = 0 #Set initiall Value For a

while True:
    a = a + 1
        #Creat a frame object
    check,frame = video.read()
    print(check)
    print(frame) #Representing image
                 #Converting to Gray scale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #Show the frame
    cv2.imshow("Capturing", gray)
                #For to press anything to out(milisecond)
    #cv2.waitKey(0)    #Enable or disable this code for waitkey
                #For Playing
    key=cv2.waitKey(1)
    if key == ord('q'): #for stop the process
        break
print(a)
        #Shutdown The Camera
video.release()
cv2.destroyAllWindows()