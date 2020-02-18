class Image:
    def __init__(self, image):
        self.image = image

    def transpose(self):
        for i in range(len(self.image)):
            for j in range(len(self.image)):
                if j >= i:
                    temp = self.image[i][j]
                    self.image[i][j] = self.image[j][i]
                    self.image[j][i] = temp

    def flip(self):
        for j in range(int(len(self.image)/2)):
            for i in range(len(self.image)):
                temp = self.image[i][j]
                self.image[i][j] = self.image[i][len(self.image)-1-j]
                self.image[i][len(self.image)-1-j] = temp
        

    def printMatrix(self):
        print(self.image)

image = Image([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
image.printMatrix()
image.transpose()
image.printMatrix()
image.flip()
image.printMatrix()