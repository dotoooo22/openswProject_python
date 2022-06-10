import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
file_path = os.path.dirname(os.path.realpath(__file__))  ##현재디렉토리경로
draw_class = uic.loadUiType(file_path + "/design.ui")[0]

class CWidget(QWidget, draw_class): 
 
    def __init__(self):
 
        super().__init__()
        self.setupUi(self)
        
        
        self.line.clicked.connect(self.radioClicked)
        self.curve.clicked.connect(self.radioClicked)
        self.rectangle.clicked.connect(self.radioClicked)
        self.ellipse.clicked.connect(self.radioClicked)
        
        self.pen_color_choice.clicked.connect(self.showColorDlg)
        self.brush_color_choice.clicked.connect(self.showColorDlg)
        
        self.drawType = -1
         
    def radioClicked(self):
        if(self.line.isChecked()):
            self.drawType = 0
        elif(self.curve.isChecked()):
            self.drawType = 1
        elif(self.rectangle.isChecked()):
            self.drawType = 2
        elif(self.ellipse.isChecked()):
            self.drawType = 3
        print(self.drawType)
 
    def checkClicked(self):
        pass
             
    def showColorDlg(self):       
         
        # 색상 대화상자 생성      
        color = QColorDialog.getColor()
 
        sender = self.sender()
 
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if sender == self.pen_color_choice and color.isValid():           
            self.pencolor = color
            self.pen_color_choice.setStyleSheet('background-color: {}'.format( color.name()))
        else:
            self.brushcolor = color
            self.brush_color_choice.setStyleSheet('background-color: {}'.format( color.name()))
            
class CView(QGraphicsView):
    def __init__(self, parent):
 
        super().__init__(parent)
        self.scene = QGraphicsScene()        
        self.setScene(self.scene)
        self.items = []
        self.start = QPointF()
        self.end = QPointF()
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        
        
    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0,0,-2,-2)
 
        self.scene.setScenerect(rect)
 
    def mousePressEvent(self, e):
 
        if e.button() == Qt.LeftButton:
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()        
 
    def mouseMoveEvent(self, e):  
         
        # e.gb_1()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴 
        if e.buttons() & Qt.LeftButton:           
 
            self.end = e.pos()
 
            if self.parent().checkbox.isChecked():
                pen = QPen(QColor(255,255,255), 10)
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
                self.start = e.pos()
                return None
 
            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
            # 직선 그리기
            if self.parent().drawType == 0:
                 
                # 장면에 그려진 이전 선을 제거            
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])                
 
                # 현재 선 추가
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())                
                self.items.append(self.scene.addLine(line, pen))
 
            # 곡선 그리기
            if self.parent().drawType == 1:
 
                # Path 이용
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
 
                # Line 이용
                #line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                #self.scene.addLine(line, pen)
                 
                # 시작점을 다시 기존 끝점으로
                self.start = e.pos()
 
            # 사각형 그리기
            if self.parent().drawType == 2:
                brush = QBrush(self.parent().brushcolor)
 
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])
 
 
                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addrect(rect, pen, brush))
                 
            # 원 그리기
            if self.parent().drawType == 3:
                brush = QBrush(self.parent().brushcolor)
 
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])
 
 
                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addEllipse(rect, pen, brush))
 
 
    def mouseReleaseEvent(self, e):        
 
        if e.button() == Qt.LeftButton:
 
            if self.parent().checkbox.isChecked():
                return None
 
            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
            if self.parent().drawType == 0:
 
                self.items.clear()
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                 
                self.scene.addLine(line, pen)
 
            if self.parent().drawType == 2:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addrect(rect, pen, brush)
 
            if self.parent().drawType == 3:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addEllipse(rect, pen, brush)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())