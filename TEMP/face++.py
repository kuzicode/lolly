'''
基于face++的API，实现人脸识别功能
'''
import requests

def face_recognition(pic_1,pic_2):
	'''
	上传本地的两个图片，用于识别是否是同一个人(人脸识别)
	:pic_1,pic_2: local picture path
	:rtype:json
	'''
	url='https://api-cn.faceplusplus.com/facepp/v3/compare'
	
	data={
		'api_key':'ku-OGYH-G5ohgFtogUbox5rT0RHtNJK6',
		'api_secret':'ZGmzUzNJPDUP-J4UDmr4JEnq89h6zxSI'}	
	files={'image_file1':open(pic_1,'rb'),'image_file2':open(pic_2,'rb')}

	print(requests.post(url,data=data,files=files).text)

def face_recognition_online(url_1,url_2):
	'''
	和上一个函数的功能一样，区别在于需要传入两个图片的url
	'''
	url='https://api-cn.faceplusplus.com/facepp/v3/compare'
	data={
			'api_key':'ku-OGYH-G5ohgFtogUbox5rT0RHtNJK6',
			'api_secret':'ZGmzUzNJPDUP-J4UDmr4JEnq89h6zxSI',
			'image_url1':url_1,
			'image_url2':url_2
		}
	print(requests.post(url,data=data).text)

if __name__ == '__main__':
	# face_recognition('e:/1.jpg','e:/2.jpg')
	url1='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1519388599421&di=c56873a9a3054b3d964d5f4a77f6835e&imgtype=0&src=http%3A%2F%2Fp8.qhimg.com%2Ft01d5fe9c95c53e0a23.jpg'
	url2='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1519388594927&di=dbe88145f2875c1efa207de89f8c726c&imgtype=0&src=http%3A%2F%2Fwww.hinews.cn%2Fpic%2F0%2F10%2F66%2F81%2F10668118_229242.jpg'

	# face_recognition_online(url1,url2)
	img1='1.jpg'
	img2='6.jpg'
	face_recognition(img1,img2)
