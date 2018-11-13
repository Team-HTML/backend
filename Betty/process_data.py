import shape_detect1 as detector 
import os 
import cv2

#the img decides the original or the preprocessed one to be cut 
def cut_each(img, num, path, white): 
	img1 = detector.preprocess(img)
	small2 = cv2.resize(img1, (0,0), fx=0.2, fy=0.2)
	cv2.imshow("try", small2);
	k = cv2.waitKey(1000) # 0==wait forever
	contour = detector.contour(img1)
	rect = detector.rect_to_cut(contour)
	detector.cut(img, rect, num, path, white)

def dataset(num_pic, output_path, input_path, white): 
	for i in range(20,num_pic+1): 
		print("THE NUMBER OF THE PIC, ", i)
		target = str(i) + '.jpg'
		img = cv2.imread(os.path.join(input_path, target))
		#if img == None: 
		#	print("You Are Stupid!")
		cut_each(img, i, output_path, white) 


output_path = '/Users/bettyzhou/Desktop/cse110_ml/after_cut_training_sets'
output_path2 = '/Users/bettyzhou/Desktop/cse110_ml/original_cut_training_sets'
input_path = '/Users/bettyzhou/Desktop/cse110_ml/DRAWINGS'
white = cv2.imread('white.jpg')
white = cv2.resize(white, (1800,1800))


dataset(25,output_path,input_path,white)


#img = cv2.imread(os.path.join(input_path, str(5)+'.jpg'))
#if img == None: 
#	print("OWWW")
#small2 = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
#cv2.imshow("try", small2);
#k = cv2.waitKey(1000) # 0==wait forever

#cv2.destroyAllWindows()
#
#img = cv2.imread(os.path.join(input_path, str(1)+'.jpg'))
#white1 = detector.preprocess(img)
#white1, d = cut_each(img, 0, 1, output_path, white)
#pic = detector.preprocess(img)
#small2 = cv2.resize(white1, (0,0), fx=0.2, fy=0.2)
#print("THIS IS AFTER")
#cv2.imshow("try", small2);
#k = cv2.waitKey(2000) # 0==wait forever
#cv2.destroyAllWindows()



