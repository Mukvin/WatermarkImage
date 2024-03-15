from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QLineEdit, QComboBox, QSlider
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import os
import sys

from utils.add_watermark import add_watermark


class WatermarkApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watermark App")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel("Image Path:")
        layout.addWidget(self.image_label)

        self.image_path_label = QLabel()
        layout.addWidget(self.image_path_label)

        self.select_image_button = QPushButton("Select Image")
        self.select_image_button.clicked.connect(self.select_image)
        layout.addWidget(self.select_image_button)

        self.output_label = QLabel("Output Path:")
        layout.addWidget(self.output_label)

        self.output_path_label = QLabel()
        layout.addWidget(self.output_path_label)

        self.select_output_button = QPushButton("Select Output")
        self.select_output_button.clicked.connect(self.select_output)
        layout.addWidget(self.select_output_button)

        self.watermark_text_label = QLabel("Watermark Text:")
        layout.addWidget(self.watermark_text_label)

        self.watermark_text_edit = QLineEdit()
        layout.addWidget(self.watermark_text_edit)

        self.font_label = QLabel("Font:")
        layout.addWidget(self.font_label)

        self.font_list = os.listdir("fonts")
        self.font_combo_box = QComboBox()
        self.font_combo_box.addItems(self.font_list)
        layout.addWidget(self.font_combo_box)

        self.font_size_label = QLabel("Font Size:")
        layout.addWidget(self.font_size_label)

        self.font_size_combo_box = QComboBox()
        self.font_size_combo_box.addItems([str(i) for i in range(20, 40)])
        layout.addWidget(self.font_size_combo_box)

        self.opacity_label = QLabel("Opacity:")
        layout.addWidget(self.opacity_label)

        self.opacity_slider = QSlider(Qt.Horizontal)
        self.opacity_slider.setMinimum(0)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(50)
        self.opacity_slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.opacity_slider)

        self.watermark_button = QPushButton("Add Watermark")
        self.watermark_button.clicked.connect(self.add_watermark)
        layout.addWidget(self.watermark_button)

    def select_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        self.image_path_label.setText(image_path)

    def select_output(self):
        output_path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        self.output_path_label.setText(output_path)

    def add_watermark(self):
        image_path = self.image_path_label.text()
        output_path = self.output_path_label.text()
        watermark_text = self.watermark_text_edit.text()
        font_file = os.path.join("fonts", self.font_combo_box.currentText())
        font_size = int(self.font_size_combo_box.currentText())
        opacity = self.opacity_slider.value() / 100

        if image_path and output_path and watermark_text:
            add_watermark(image_path, watermark_text, output_path, font_file, font_size, opacity)
            self.image_path_label.clear()
            self.output_path_label.clear()
            self.watermark_text_edit.clear()
