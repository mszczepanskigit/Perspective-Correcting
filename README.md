README

# Perspective-Correction
Program to correct perspective of grabbed area in given image. You can see how it works with apple.jpg and new_apple.jpg images.

perspective.py is the usable file from the command line.

Just type:
		"python perspective.py <input_image_name> <output_image_name> <height_of_output> <width_of_output>"
    
IMPORTANT!!
  While Grabbing an area you have to grab in special order. Firstly you have to grab left upper corner, then right upper, right bottom and left bottom corners. In     the other case program can break down or give bad output. Contact with me if you have any problem.
  
Used packages:
	- NumPy
	- OpenCV
    
Below program has been created thanks to Python-Minicourse about image processing by InterTech Academy (Maciej Kraszewski) on Udemy.  
