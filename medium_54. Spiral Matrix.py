class Solution(object):
    def spiralOrder(self, inputMatrix):
          output = []
          while inputMatrix:
            output.extend(inputMatrix.pop(0))
            if inputMatrix and inputMatrix[0]:
              output.extend([i.pop() for i in inputMatrix])
            if inputMatrix and inputMatrix[0]:
              output.extend(inputMatrix.pop()[::-1])
            if inputMatrix and inputMatrix[0]:
              output.extend([i.pop(0) for i in inputMatrix][::-1])
          return output
