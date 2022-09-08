import cv2
import os
import string

cap = cv2.VideoCapture(0)
#setting fixed size for opencv frame
width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(0,10):
    if not os.path.exists("data/" + str(i)):
        os.makedirs("data/"+str(i))


for i in string.ascii_uppercase:
    if not os.path.exists("data/" + str(i)):
        os.makedirs("data/"+str(i))

if not os.path.exists("data/BLANK"):
    os.mkdir("data/BLANK")

while (True):

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    count = {
        'zero': len(os.listdir("data/" + "/0")),
        'one': len(os.listdir("data/" + "/1")),
        'two': len(os.listdir("data/" + "/2")),
        'three': len(os.listdir("data/"+"/3")),
        'four': len(os.listdir("data/"+"/4")),
        'five': len(os.listdir("data/"+"/5")),
        'six': len(os.listdir("data/"+"/6")),
        'seven': len(os.listdir("data/" + "/7")),
        'eight': len(os.listdir("data/" + "/8")),
        'nine': len(os.listdir("data/" + "/9")),
        'a': len(os.listdir("data/" + "/A")),
        'b': len(os.listdir("data/" + "/B")),
        'c': len(os.listdir("data/" + "/C")),
        'd': len(os.listdir("data/" + "/D")),
        'e': len(os.listdir("data/" + "/E")),
        'f': len(os.listdir("data/" + "/F")),
        'g': len(os.listdir("data/" + "/G")),
        'h': len(os.listdir("data/" + "/H")),
        'i': len(os.listdir("data/" + "/I")),
        'j': len(os.listdir("data/" + "/J")),
        'k': len(os.listdir("data/" + "/K")),
        'l': len(os.listdir("data/" + "/L")),
        'm': len(os.listdir("data/" + "/M")),
        'n': len(os.listdir("data/" + "/N")),
        'o': len(os.listdir("data/" + "/O")),
        'p': len(os.listdir("data/" + "/P")),
        'q': len(os.listdir("data/" + "/Q")),
        'r': len(os.listdir("data/" + "/R")),
        's': len(os.listdir("data/" + "/S")),
        't': len(os.listdir("data/" + "/T")),
        'u': len(os.listdir("data/" + "/U")),
        'v': len(os.listdir("data/" + "/V")),
        'w': len(os.listdir("data/" + "/W")),
        'x': len(os.listdir("data/" + "/X")),
        'y': len(os.listdir("data/" + "/Y")),
        'z': len(os.listdir("data/" + "/Z")),
        'blank': len(os.listdir("data/" + "/BLANK"))
    }
    
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 80), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "FIVE : "+str(count['five']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "SIX : "+str(count['six']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "SEVEN : " + str(count['seven']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "EIGHT : " + str(count['eight']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "NINE : " + str(count['nine']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "a : "+str(count['a']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "b : "+str(count['b']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "c : "+str(count['c']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "d : "+str(count['d']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "e : "+str(count['e']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "f : "+str(count['f']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "g : "+str(count['g']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "h : "+str(count['h']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "i : "+str(count['i']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "j : " + str(count['j']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
    cv2.putText(frame, "k : "+str(count['k']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "l : "+str(count['l']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "m : "+str(count['m']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "n : "+str(count['n']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "o : "+str(count['o']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "p : "+str(count['p']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "q : "+str(count['q']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "r : "+str(count['r']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "s : "+str(count['s']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "t : "+str(count['t']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "u : "+str(count['u']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "v : "+str(count['v']), (10, 380), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "w : "+str(count['w']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "x : "+str(count['x']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "y : "+str(count['y']), (10, 410), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "z : "+str(count['z']), (10, 420), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(frame, "blank : " + str(count['blank']), (10, 430), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)

    #Capturing region of Interest
    roi = cv2.rectangle(frame,(340,20),(630,260),(255,0,0),2)

    #Extract grayscale image image of roi and removing noise using Gaussian blur
    extract= frame[20:260,340:630]
    gray = cv2.cvtColor(extract, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, test_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    # Display the resulting frame
    cv2.imshow('Gray',gray)
    cv2.imshow('frame', frame)
    cv2.imshow("test", test_image)


    if cv2.waitKey(1) & 0xFF == ord('#'):
        break
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite('data/'+'0/'+str(count['zero'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite('data/'+'1/'+str(count['one'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite('data/'+'2/'+str(count['two'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite('data/'+'3/'+str(count['three'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite('data/'+'4/'+str(count['four'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite('data/'+'5/'+str(count['five'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite('data/'+'6/'+str(count['six'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite('data/'+'7/'+str(count['seven'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite('data/'+'8/'+str(count['eight'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite('data/'+'9/'+str(count['nine'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite('data/'+'A/'+str(count['a'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite('data/'+'B/'+str(count['b'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite('data/'+'C/'+str(count['c'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite('data/'+'D/'+str(count['d'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite('data/'+'E/'+str(count['e'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite('data/'+'F/'+str(count['f'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite('data/'+'G/'+str(count['g'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite('data/'+'H/'+str(count['h'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite('data/'+'I/'+str(count['i'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite('data/'+'J/'+str(count['j'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite('data/'+'K/'+str(count['k'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite('data/'+'L/'+str(count['l'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite('data/'+'M/'+str(count['m'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite('data/'+'N/'+str(count['n'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite('data/'+'O/'+str(count['o'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite('data/'+'P/'+str(count['p'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite('data/'+'Q/'+str(count['q'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite('data/'+'R/'+str(count['r'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite('data/'+'S/'+str(count['s'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite('data/'+'T/'+str(count['t'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite('data/'+'U/'+str(count['u'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite('data/'+'V/'+str(count['v'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite('data/'+'W/'+str(count['w'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite('data/'+'X/'+str(count['x'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite('data/'+'Y/'+str(count['y'])+'.jpg', test_image)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite('data/'+'Z/'+str(count['z'])+'.jpg', test_image)
    if interrupt & 0xFF == ord(' '):
        cv2.imwrite('data/'+'BLANK/'+str(count['blank'])+'.jpg', test_image)
    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
