import time, sensor, image, os, uos, gc
from image import SEARCH_EX, SEARCH_DS
from machine import UART
import ustruct
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.skip_frames(time=12000)
uart = UART(3, 115200)
red_thresholds = [(30, 100, 15, 127, 15, 127),(34, 66, 7, -61, 87, 18)]
dog_thresholds = [(34, 66, 7, -61, 87, 18)]
door_thresholds = [(6, 87, 9, 86, 52, -2)]
templates = [
	image.Image("./pgm_files/left.pgm"),
	image.Image("./pgm_files/left1.pgm"),
	image.Image("./pgm_files/left2.pgm"),
	image.Image("./pgm_files/left3.pgm"),
	image.Image("./pgm_files/left4.pgm"),
	image.Image("./pgm_files/left5.pgm"),
	image.Image("./pgm_files/left6.pgm"),
	image.Image("./pgm_files/left7.pgm"),
	image.Image("./pgm_files/right.pgm"),
	image.Image("./pgm_files/right1.pgm"),
	image.Image("./pgm_files/right2.pgm"),
	image.Image("./pgm_files/right3.pgm"),
	image.Image("./pgm_files/right4.pgm"),
	image.Image("./pgm_files/right5.pgm"),
	image.Image("./pgm_files/right6.pgm"),
	image.Image("./pgm_files/right7.pgm"),
	image.Image("./pgm_files/straight.pgm"),
	image.Image("./pgm_files/straight1.pgm"),
	image.Image("./pgm_files/straight2.pgm"),
	image.Image("./pgm_files/straight3.pgm"),
	image.Image("./pgm_files/straight4.pgm"),
	image.Image("./pgm_files/straight5.pgm"),
	image.Image("./pgm_files/straight6.pgm"),
	image.Image("./pgm_files/straight7.pgm")
]
barricade_templates = [
	image.Image("./pgm_files/barricade.pgm"),
	image.Image("./pgm_files/barricade1.pgm"),
	image.Image("./pgm_files/barricade2.pgm")
]
traffic_light_templates = [
	image.Image("./pgm_files/traffic-light1.pgm"),
	image.Image("./pgm_files/traffic-light2.pgm"),
	image.Image("./pgm_files/traffic-light3.pgm"),
	image.Image("./pgm_files/traffic-light4.pgm"),
	image.Image("./pgm_files/traffic-light5.pgm"),
	image.Image("./pgm_files/traffic-light6.pgm"),
	image.Image("./pgm_files/traffic-light7.pgm"),
	image.Image("./pgm_files/traffic-light8.pgm"),
	image.Image("./pgm_files/traffic-light9.pgm"),
	image.Image("./pgm_files/traffic-light10.pgm"),
	image.Image("./pgm_files/traffic-light11.pgm"),
	image.Image("./pgm_files/traffic-light12.pgm"),
	image.Image("./pgm_files/traffic-light13.pgm"),
	image.Image("./pgm_files/traffic-light14.pgm"),
	image.Image("./pgm_files/traffic-light15.pgm")
]
clock = time.clock()
barricades_count = 0
red_light_count = 0
right_arrow_count = 0
left_arrow_count = 0
straight_arrow_count = 0
dog_count = 0
door_count = 0
go=0
no_red_light_frames = 0
no_dog_frames = 0
loading_stage = 'arrows'
while True:
	clock.tick()
	img_rgb = sensor.snapshot()
	img = img_rgb.to_grayscale(copy=True)
	template_matching = False
	if loading_stage == 'arrows':
		current_templates = templates
	elif loading_stage == 'traffic_lights':
		current_templates = traffic_light_templates
	elif loading_stage == 'barricades':
		current_templates = barricade_templates
	else:
		current_templates = []
	for idx, template in enumerate(current_templates):
		r = img.find_template(template, 0.80, step=4, search=SEARCH_EX)
		if r:
			template_matching = True
			img_rgb.draw_rectangle(r)
			if loading_stage == 'arrows':
				if idx in { 0,1,2, 3, 4, 5, 6,7}:
					print("left")
					left_arrow_count += 1
				elif idx in {8,9,10, 11, 12, 13,14,15}:
					print("right")
					right_arrow_count += 1
				elif idx in {16,17,18, 19,20,21,22,23}:
					print("straight")
					straight_arrow_count += 1
			elif loading_stage == 'traffic_lights':
				print("traffic Color Code")
				roi = (r[0], r[1], r[2], r[3])
				for blob in img_rgb.find_blobs(red_thresholds, roi=roi, pixels_threshold=20, area_threshold=50):
					img_rgb.draw_rectangle(blob.rect())
					img_rgb.draw_cross(blob.cx(), blob.cy())
					print("Blob Color Code:", blob.code())
					if blob.code() == 1:
						red_light_count += 1
						no_red_light_frames=0
					else:
						no_red_light_frames += 1
						print(' no_red_light_frames {no_red_light_frames}')
			elif loading_stage == 'barricades':
				print(f"barricade{idx}")
				barricades_count += 1
			break
	if  template_matching == 0 and loading_stage == 'dog_detection':
		print("Dog Color Code")
		no_dog_frames += 1
		for blob in img_rgb.find_blobs(dog_thresholds, pixels_threshold=20, area_threshold=50):
			img_rgb.draw_rectangle(blob.rect())
			img_rgb.draw_cross(blob.cx(), blob.cy())
			print("Dog Color Code:", blob.code())
			if blob.code() == 1:
				dog_count += 1
				print(blob.code())
				no_dog_frames = 0
			else:
				no_dog_frames += 1
				print("no_dog_frames += 1")
	if template_matching ==0 and loading_stage == 'door_detection':
		print("final detection")
		for blob in img_rgb.find_blobs(door_thresholds,pixels_threshold=20, area_threshold=50 ):
			img_rgb.draw_rectangle(blob.rect())
			img_rgb.draw_cross(blob.cx(), blob.cy())
			print("door Color Code:", blob.code())
			if blob.code() == 1:
				door_count += 1
	send_data = ""
	if red_light_count > 0:
		send_data = "1"
		red_light_count = 0
	elif no_red_light_frames >2:
		send_data = "2"
		no_red_light_frames = 0
	elif barricades_count > 15:
		send_data = "3"
		barricades_count = 0
	elif dog_count > 2:
		send_data = "9"
		dog_count = 0
	elif no_dog_frames>60:
		send_data = "8"
		no_dog_frames = 0
	elif left_arrow_count > 1:
		send_data = "6"
		left_arrow_count = 0
	elif right_arrow_count > 1:
		send_data = "5"
		right_arrow_count = 0
	elif straight_arrow_count > 1:
		send_data = "7"
		straight_arrow_count = 0
	elif door_count>5:
		sensor.skip_frames(time=3000)
		send_data = ":"
		door_count=0
	elif go>0:
		send_data="4"
		g0=0
		print("go!!!!!")
		uart.write(send_data)
		print(send_data)
		break
	if send_data:
		uart.write(send_data)
		print(send_data)
		if send_data in ["5", "6", "7"]:
			loading_stage = 'traffic_lights'
			templates = traffic_light_templates
		elif send_data == "2":
			traffic_light_detected=False
			print("开始暂停")
			sensor.skip_frames(time=9000)
			print("暂停结束")
			loading_stage = 'dog_detection'
		elif send_data == "8":
			loading_stage = 'barricades'
		elif send_data == '3':
			loading_stage='door_detection'
			sensor.skip_frames(time=5000)
		elif send_data == ':':
			sensor.skip_frames(time=5000)
			go+=1
	del img_rgb
	del img
	gc.collect()