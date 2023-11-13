from adaptive_threshold import adaptive_threshold
from closing import closing_filter
from computer_visions.beginner.canny.canny import canny_filter
from computer_visions.beginner.contours.contours import find_contours
from computer_visions.beginner.contours.point_detection import point_detection
from connected_components import connected_components
from dilation import dilation
from erosion import erosion
from global_threshold import global_threshold
from opening import opening_filter
from thickening import thickening_filter
from thinning import thinning_filter

# todo canny filter
cannyImage = r'D:\Projcets\py\assets\beginner\canny\canny1.jpg'

# todo contours filter
contoursImage = r'D:\Projcets\py\assets\beginner\contours\contours.png'

# todo point filter
pointImage = r'D:\Projcets\py\assets\beginner\contours\img.png'

# todo face_rec filter
face_recImage = r'D:\Projcets\py\assets\beginner\face_rec\face_rec.png'

# todo erosion filter
erosionImage = r'D:\Projcets\py\assets\basics\erosion\erosion.png'

# todo opening filter
openingImage = r'D:\Projcets\py\assets\basics\opening\img.png'


connected_components(openingImage)