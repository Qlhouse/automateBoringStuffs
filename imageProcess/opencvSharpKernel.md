# 什么是核

在图像处理中许多滤波器（滤波函数）都会使用核（kernel）。

核其实是一组权重，决定了如何利用某一个点周围的像素点来计算新的像素点，核也称为卷积矩阵，对一个区域的像素做调和或者卷积运算，通常基于核的滤波器被称为卷积滤波器。OpenCV中的filter2D()函数，可以运用由用户指定的任意核来计算。

# 核的格式

核通常是一个二位数组，特征是奇数行，奇数列，中心位置对应着感兴趣的像素，数组每一个元素为整数或者浮点数，相对应值的大小对应其权重，比如

`kernel = numpy.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])`

表明感兴趣的像素值权重为9，相邻区域权重为-1，而计算则为将中心像素值乘以9，减去周围所有的像素，如果感兴趣的像素与周围像素存在差异，则该差异会被放大，达到了锐化的目的

[wiki-Kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing))

In image processing, a **kernel, convolution matrix**, or **mask** is a small matrix. It's used for blurring, sharpening, embossing, edge detection, and more. This is accomplished by doing a convolution between a kernel and an image.


