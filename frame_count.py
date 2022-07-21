import cv2

# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output_frames/output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(cv2.samples.findFile('videos/new/b_1_50_percent.avi'))
# cap = cv2.VideoCapture(cv2.samples.findFile("result_ball_right.mp4"))
i = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    # incase video ends.
    if ret == False or (cv2.waitKey(10) & 0xFF == ord('q')):
        # cv2.imwrite('output_frames/' + 'Last_Frame_from_Right_Image' + str(i) + '.jpg', frame)
        print("total frame:" + str(i))
        break

    i += 1

    # if (i >= 20):
    #     out.write(frame)

cap.release()
cv2.destroyAllWindows()