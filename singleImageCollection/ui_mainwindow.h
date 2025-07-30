/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>
#include "QEComboBox.h"
#include "QEFileBrowser.h"
#include "QEImage.h"
#include "QELabel.h"
#include "QELineEdit.h"
#include "QEPushButton.h"
#include "QERadioButton.h"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *layoutWidget;
    QGridLayout *gridLayout_2;
    QHBoxLayout *horizontalLayout_2;
    QEComboBox *selectCamera;
    QLabel *cameraSelected;
    QHBoxLayout *horizontalLayout_3;
    QEPushButton *restartIOC;
    QEPushButton *setDefaults;
    QHBoxLayout *horizontalLayout_12;
    QLabel *label_5;
    QELabel *status;
    QHBoxLayout *horizontalLayout_8;
    QLabel *label_6;
    QELabel *imgCounter;
    QHBoxLayout *horizontalLayout;
    QLabel *label_7;
    QELabel *pixelFormat;
    QLabel *label_8;
    QSpacerItem *horizontalSpacer;
    QLabel *label_3;
    QELabel *xDim;
    QLabel *label_2;
    QELabel *yDim;
    QLabel *label_4;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_9;
    QEComboBox *lightCondition;
    QGridLayout *gridLayout;
    QLabel *label_21;
    QLabel *label_27;
    QPushButton *resetROI;
    QELineEdit *r1y2;
    QLabel *label_18;
    QLabel *label_29;
    QELineEdit *r3y1;
    QELineEdit *r4y2;
    QLabel *label_32;
    QLabel *label_17;
    QLabel *label_22;
    QLabel *label_30;
    QLabel *label_23;
    QELineEdit *r4x2;
    QLabel *label_20;
    QLabel *label_14;
    QLabel *label_16;
    QLabel *label_28;
    QELineEdit *r1x2;
    QELineEdit *r1x1;
    QELineEdit *r2y2;
    QLabel *label_26;
    QELineEdit *r3x2;
    QELineEdit *r2x1;
    QLabel *label_33;
    QELineEdit *r2y1;
    QLabel *label_24;
    QLabel *label_15;
    QELineEdit *r1y1;
    QLabel *label_19;
    QELineEdit *r3y2;
    QLabel *label_31;
    QELineEdit *r4x1;
    QLabel *label_25;
    QELineEdit *r3x1;
    QELineEdit *r4y1;
    QELineEdit *r2x2;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_12;
    QERadioButton *good;
    QERadioButton *bad;
    QHBoxLayout *horizontalLayout_13;
    QLabel *label_11;
    QEComboBox *extension;
    QHBoxLayout *horizontalLayout_9;
    QLabel *label_13;
    QELineEdit *expTime;
    QHBoxLayout *horizontalLayout_11;
    QEPushButton *stream;
    QEPushButton *stop;
    QPushButton *saveROI;
    QEFileBrowser *fileListing;
    QSplitter *splitter;
    QEImage *qeimage;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1050, 750);
        MainWindow->setMinimumSize(QSize(1050, 750));
        MainWindow->setMaximumSize(QSize(1050, 750));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        layoutWidget = new QWidget(centralwidget);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 11, 471, 667));
        gridLayout_2 = new QGridLayout(layoutWidget);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        selectCamera = new QEComboBox(layoutWidget);
        selectCamera->addItem(QString());
        selectCamera->addItem(QString());
        selectCamera->addItem(QString());
        selectCamera->setObjectName(QString::fromUtf8("selectCamera"));
        selectCamera->setAutoFillBackground(false);

        horizontalLayout_2->addWidget(selectCamera);

        cameraSelected = new QLabel(layoutWidget);
        cameraSelected->setObjectName(QString::fromUtf8("cameraSelected"));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        font.setWeight(75);
        cameraSelected->setFont(font);
        cameraSelected->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(cameraSelected);


        gridLayout_2->addLayout(horizontalLayout_2, 0, 0, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        restartIOC = new QEPushButton(layoutWidget);
        restartIOC->setObjectName(QString::fromUtf8("restartIOC"));
        QPalette palette;
        QBrush brush(QColor(255, 0, 0, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush);
        restartIOC->setPalette(palette);
        restartIOC->setCursor(QCursor(Qt::PointingHandCursor));

        horizontalLayout_3->addWidget(restartIOC);

        setDefaults = new QEPushButton(layoutWidget);
        setDefaults->setObjectName(QString::fromUtf8("setDefaults"));
        QPalette palette1;
        QBrush brush1(QColor(0, 170, 255, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette1.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        setDefaults->setPalette(palette1);
        setDefaults->setCursor(QCursor(Qt::PointingHandCursor));

        horizontalLayout_3->addWidget(setDefaults);


        gridLayout_2->addLayout(horizontalLayout_3, 1, 0, 1, 1);

        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        label_5 = new QLabel(layoutWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_12->addWidget(label_5);

        status = new QELabel(layoutWidget);
        status->setObjectName(QString::fromUtf8("status"));

        horizontalLayout_12->addWidget(status);


        gridLayout_2->addLayout(horizontalLayout_12, 2, 0, 1, 1);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        label_6 = new QLabel(layoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_8->addWidget(label_6);

        imgCounter = new QELabel(layoutWidget);
        imgCounter->setObjectName(QString::fromUtf8("imgCounter"));

        horizontalLayout_8->addWidget(imgCounter);


        gridLayout_2->addLayout(horizontalLayout_8, 3, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_7 = new QLabel(layoutWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setFrameShape(QFrame::StyledPanel);

        horizontalLayout->addWidget(label_7);

        pixelFormat = new QELabel(layoutWidget);
        pixelFormat->setObjectName(QString::fromUtf8("pixelFormat"));

        horizontalLayout->addWidget(pixelFormat);

        label_8 = new QLabel(layoutWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setFrameShape(QFrame::StyledPanel);

        horizontalLayout->addWidget(label_8);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        label_3 = new QLabel(layoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout->addWidget(label_3);

        xDim = new QELabel(layoutWidget);
        xDim->setObjectName(QString::fromUtf8("xDim"));

        horizontalLayout->addWidget(xDim);

        label_2 = new QLabel(layoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout->addWidget(label_2);

        yDim = new QELabel(layoutWidget);
        yDim->setObjectName(QString::fromUtf8("yDim"));

        horizontalLayout->addWidget(yDim);

        label_4 = new QLabel(layoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout->addWidget(label_4);


        gridLayout_2->addLayout(horizontalLayout, 4, 0, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        label_9 = new QLabel(layoutWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_6->addWidget(label_9);

        lightCondition = new QEComboBox(layoutWidget);
        lightCondition->setObjectName(QString::fromUtf8("lightCondition"));
        lightCondition->setCursor(QCursor(Qt::PointingHandCursor));
        lightCondition->setAutoFillBackground(false);
        lightCondition->setEditable(false);

        horizontalLayout_6->addWidget(lightCondition);


        gridLayout_2->addLayout(horizontalLayout_6, 5, 0, 1, 1);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_21 = new QLabel(layoutWidget);
        label_21->setObjectName(QString::fromUtf8("label_21"));

        gridLayout->addWidget(label_21, 1, 7, 1, 1);

        label_27 = new QLabel(layoutWidget);
        label_27->setObjectName(QString::fromUtf8("label_27"));

        gridLayout->addWidget(label_27, 2, 1, 1, 1);

        resetROI = new QPushButton(layoutWidget);
        resetROI->setObjectName(QString::fromUtf8("resetROI"));

        gridLayout->addWidget(resetROI, 4, 2, 1, 7);

        r1y2 = new QELineEdit(layoutWidget);
        r1y2->setObjectName(QString::fromUtf8("r1y2"));

        gridLayout->addWidget(r1y2, 0, 8, 1, 1);

        label_18 = new QLabel(layoutWidget);
        label_18->setObjectName(QString::fromUtf8("label_18"));

        gridLayout->addWidget(label_18, 0, 7, 1, 1);

        label_29 = new QLabel(layoutWidget);
        label_29->setObjectName(QString::fromUtf8("label_29"));

        gridLayout->addWidget(label_29, 3, 5, 1, 1);

        r3y1 = new QELineEdit(layoutWidget);
        r3y1->setObjectName(QString::fromUtf8("r3y1"));

        gridLayout->addWidget(r3y1, 2, 4, 1, 1);

        r4y2 = new QELineEdit(layoutWidget);
        r4y2->setObjectName(QString::fromUtf8("r4y2"));

        gridLayout->addWidget(r4y2, 3, 8, 1, 1);

        label_32 = new QLabel(layoutWidget);
        label_32->setObjectName(QString::fromUtf8("label_32"));

        gridLayout->addWidget(label_32, 3, 1, 1, 1);

        label_17 = new QLabel(layoutWidget);
        label_17->setObjectName(QString::fromUtf8("label_17"));

        gridLayout->addWidget(label_17, 0, 5, 1, 1);

        label_22 = new QLabel(layoutWidget);
        label_22->setObjectName(QString::fromUtf8("label_22"));

        gridLayout->addWidget(label_22, 1, 0, 1, 1);

        label_30 = new QLabel(layoutWidget);
        label_30->setObjectName(QString::fromUtf8("label_30"));

        gridLayout->addWidget(label_30, 3, 3, 1, 1);

        label_23 = new QLabel(layoutWidget);
        label_23->setObjectName(QString::fromUtf8("label_23"));

        gridLayout->addWidget(label_23, 1, 1, 1, 1);

        r4x2 = new QELineEdit(layoutWidget);
        r4x2->setObjectName(QString::fromUtf8("r4x2"));

        gridLayout->addWidget(r4x2, 3, 6, 1, 1);

        label_20 = new QLabel(layoutWidget);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        gridLayout->addWidget(label_20, 1, 3, 1, 1);

        label_14 = new QLabel(layoutWidget);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        gridLayout->addWidget(label_14, 0, 0, 1, 1);

        label_16 = new QLabel(layoutWidget);
        label_16->setObjectName(QString::fromUtf8("label_16"));

        gridLayout->addWidget(label_16, 0, 3, 1, 1);

        label_28 = new QLabel(layoutWidget);
        label_28->setObjectName(QString::fromUtf8("label_28"));

        gridLayout->addWidget(label_28, 2, 7, 1, 1);

        r1x2 = new QELineEdit(layoutWidget);
        r1x2->setObjectName(QString::fromUtf8("r1x2"));

        gridLayout->addWidget(r1x2, 0, 6, 1, 1);

        r1x1 = new QELineEdit(layoutWidget);
        r1x1->setObjectName(QString::fromUtf8("r1x1"));

        gridLayout->addWidget(r1x1, 0, 2, 1, 1);

        r2y2 = new QELineEdit(layoutWidget);
        r2y2->setObjectName(QString::fromUtf8("r2y2"));

        gridLayout->addWidget(r2y2, 1, 8, 1, 1);

        label_26 = new QLabel(layoutWidget);
        label_26->setObjectName(QString::fromUtf8("label_26"));

        gridLayout->addWidget(label_26, 2, 0, 1, 1);

        r3x2 = new QELineEdit(layoutWidget);
        r3x2->setObjectName(QString::fromUtf8("r3x2"));

        gridLayout->addWidget(r3x2, 2, 6, 1, 1);

        r2x1 = new QELineEdit(layoutWidget);
        r2x1->setObjectName(QString::fromUtf8("r2x1"));

        gridLayout->addWidget(r2x1, 1, 2, 1, 1);

        label_33 = new QLabel(layoutWidget);
        label_33->setObjectName(QString::fromUtf8("label_33"));

        gridLayout->addWidget(label_33, 3, 7, 1, 1);

        r2y1 = new QELineEdit(layoutWidget);
        r2y1->setObjectName(QString::fromUtf8("r2y1"));

        gridLayout->addWidget(r2y1, 1, 4, 1, 1);

        label_24 = new QLabel(layoutWidget);
        label_24->setObjectName(QString::fromUtf8("label_24"));

        gridLayout->addWidget(label_24, 2, 5, 1, 1);

        label_15 = new QLabel(layoutWidget);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        gridLayout->addWidget(label_15, 0, 1, 1, 1);

        r1y1 = new QELineEdit(layoutWidget);
        r1y1->setObjectName(QString::fromUtf8("r1y1"));

        gridLayout->addWidget(r1y1, 0, 4, 1, 1);

        label_19 = new QLabel(layoutWidget);
        label_19->setObjectName(QString::fromUtf8("label_19"));

        gridLayout->addWidget(label_19, 1, 5, 1, 1);

        r3y2 = new QELineEdit(layoutWidget);
        r3y2->setObjectName(QString::fromUtf8("r3y2"));

        gridLayout->addWidget(r3y2, 2, 8, 1, 1);

        label_31 = new QLabel(layoutWidget);
        label_31->setObjectName(QString::fromUtf8("label_31"));

        gridLayout->addWidget(label_31, 3, 0, 1, 1);

        r4x1 = new QELineEdit(layoutWidget);
        r4x1->setObjectName(QString::fromUtf8("r4x1"));

        gridLayout->addWidget(r4x1, 3, 2, 1, 1);

        label_25 = new QLabel(layoutWidget);
        label_25->setObjectName(QString::fromUtf8("label_25"));

        gridLayout->addWidget(label_25, 2, 3, 1, 1);

        r3x1 = new QELineEdit(layoutWidget);
        r3x1->setObjectName(QString::fromUtf8("r3x1"));

        gridLayout->addWidget(r3x1, 2, 2, 1, 1);

        r4y1 = new QELineEdit(layoutWidget);
        r4y1->setObjectName(QString::fromUtf8("r4y1"));

        gridLayout->addWidget(r4y1, 3, 4, 1, 1);

        r2x2 = new QELineEdit(layoutWidget);
        r2x2->setObjectName(QString::fromUtf8("r2x2"));

        gridLayout->addWidget(r2x2, 1, 6, 1, 1);


        gridLayout_2->addLayout(gridLayout, 6, 0, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_12 = new QLabel(layoutWidget);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_5->addWidget(label_12);

        good = new QERadioButton(layoutWidget);
        good->setObjectName(QString::fromUtf8("good"));
        good->setChecked(false);
        good->setWriteOnPress(true);

        horizontalLayout_5->addWidget(good);

        bad = new QERadioButton(layoutWidget);
        bad->setObjectName(QString::fromUtf8("bad"));
        bad->setWriteOnPress(true);

        horizontalLayout_5->addWidget(bad);


        gridLayout_2->addLayout(horizontalLayout_5, 7, 0, 1, 1);

        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        label_11 = new QLabel(layoutWidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_13->addWidget(label_11);

        extension = new QEComboBox(layoutWidget);
        extension->setObjectName(QString::fromUtf8("extension"));

        horizontalLayout_13->addWidget(extension);


        gridLayout_2->addLayout(horizontalLayout_13, 8, 0, 1, 1);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        label_13 = new QLabel(layoutWidget);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setFrameShape(QFrame::StyledPanel);

        horizontalLayout_9->addWidget(label_13);

        expTime = new QELineEdit(layoutWidget);
        expTime->setObjectName(QString::fromUtf8("expTime"));

        horizontalLayout_9->addWidget(expTime);


        gridLayout_2->addLayout(horizontalLayout_9, 10, 0, 1, 1);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        stream = new QEPushButton(layoutWidget);
        stream->setObjectName(QString::fromUtf8("stream"));
        stream->setCursor(QCursor(Qt::PointingHandCursor));

        horizontalLayout_11->addWidget(stream);

        stop = new QEPushButton(layoutWidget);
        stop->setObjectName(QString::fromUtf8("stop"));
        stop->setCursor(QCursor(Qt::PointingHandCursor));

        horizontalLayout_11->addWidget(stop);

        saveROI = new QPushButton(layoutWidget);
        saveROI->setObjectName(QString::fromUtf8("saveROI"));
        saveROI->setCursor(QCursor(Qt::PointingHandCursor));

        horizontalLayout_11->addWidget(saveROI);


        gridLayout_2->addLayout(horizontalLayout_11, 11, 0, 1, 1);

        fileListing = new QEFileBrowser(layoutWidget);
        fileListing->setObjectName(QString::fromUtf8("fileListing"));
        fileListing->setLineWidth(1);
        fileListing->setShowDirectoryPath(true);
        fileListing->setShowColumnSize(false);

        gridLayout_2->addWidget(fileListing, 9, 0, 1, 1);

        splitter = new QSplitter(centralwidget);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setGeometry(QRect(487, 9, 540, 497));
        splitter->setOrientation(Qt::Vertical);
        qeimage = new QEImage(splitter);
        qeimage->setObjectName(QString::fromUtf8("qeimage"));
        qeimage->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(qeimage->sizePolicy().hasHeightForWidth());
        qeimage->setSizePolicy(sizePolicy);
        qeimage->setMinimumSize(QSize(0, 0));
        qeimage->setMaximumSize(QSize(2000, 2048));
        qeimage->setAllowDrop(false);
        qeimage->setDisplayCursorPixelInfo(true);
        qeimage->setContrastReversal(false);
        qeimage->setProperty("logBrightness", QVariant(false));
        qeimage->setDisplayButtonBar(true);
        qeimage->setShowTime(true);
        qeimage->setProperty("timeColor", QVariant(QColor(255, 85, 0)));
        splitter->addWidget(qeimage);
        MainWindow->setCentralWidget(centralwidget);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        selectCamera->setItemText(0, QCoreApplication::translate("MainWindow", "Select Camera ...", nullptr));
        selectCamera->setItemText(1, QCoreApplication::translate("MainWindow", "Side Camera", nullptr));
        selectCamera->setItemText(2, QCoreApplication::translate("MainWindow", "Top Camera", nullptr));

        selectCamera->setProperty("variable", QVariant(QString()));
        cameraSelected->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        restartIOC->setText(QCoreApplication::translate("MainWindow", "Restart IOC", nullptr));
        setDefaults->setText(QCoreApplication::translate("MainWindow", "Set Defaults", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Statusr", nullptr));
        status->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "ID09EH-DCA-FLIR02:AI-CAM2-SIDE:AsynIO.CNCT", nullptr)));
        status->setText(QCoreApplication::translate("MainWindow", "Connect", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Image counter:", nullptr));
        imgCounter->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "ID09EH-DCA-FLIR01:AI-CAM1-UP:ArrayCounter_RBV", nullptr)));
        imgCounter->setText(QCoreApplication::translate("MainWindow", "178675", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Pixel Format:", nullptr));
        pixelFormat->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "ID09EH-DCA-FLIR02:AI-CAM2-SIDE:PixelFormat_RBV", nullptr)));
        pixelFormat->setText(QCoreApplication::translate("MainWindow", "Mono8", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "(X, Y):", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "(", nullptr));
        xDim->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "ID09EH-DCA-FLIR02:AI-CAM2-SIDE:PixelFormat_RBV", nullptr)));
        xDim->setText(QCoreApplication::translate("MainWindow", "Mono8", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", ", ", nullptr));
        yDim->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "ID09EH-DCA-FLIR02:AI-CAM2-SIDE:PixelFormat_RBV", nullptr)));
        yDim->setText(QCoreApplication::translate("MainWindow", "Mono8", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", ")", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Light condition", nullptr));
        lightCondition->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "lightCondition", nullptr)));
        label_21->setText(QCoreApplication::translate("MainWindow", "y2:", nullptr));
        label_27->setText(QCoreApplication::translate("MainWindow", "x1:", nullptr));
        resetROI->setText(QCoreApplication::translate("MainWindow", "Reset ROIs", nullptr));
        label_18->setText(QCoreApplication::translate("MainWindow", "y2:", nullptr));
        label_29->setText(QCoreApplication::translate("MainWindow", "x2:", nullptr));
        label_32->setText(QCoreApplication::translate("MainWindow", "x1:", nullptr));
        label_17->setText(QCoreApplication::translate("MainWindow", "x2:", nullptr));
        label_22->setText(QCoreApplication::translate("MainWindow", "ROI 2", nullptr));
        label_30->setText(QCoreApplication::translate("MainWindow", "y1:", nullptr));
        label_23->setText(QCoreApplication::translate("MainWindow", "x1:", nullptr));
        label_20->setText(QCoreApplication::translate("MainWindow", "y1:", nullptr));
        label_14->setText(QCoreApplication::translate("MainWindow", "ROI 1", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "y1:", nullptr));
        label_28->setText(QCoreApplication::translate("MainWindow", "y2:", nullptr));
        label_26->setText(QCoreApplication::translate("MainWindow", "ROI 3", nullptr));
        label_33->setText(QCoreApplication::translate("MainWindow", "y2:", nullptr));
        label_24->setText(QCoreApplication::translate("MainWindow", "x2:", nullptr));
        label_15->setText(QCoreApplication::translate("MainWindow", "x1:", nullptr));
        label_19->setText(QCoreApplication::translate("MainWindow", "x2:", nullptr));
        label_31->setText(QCoreApplication::translate("MainWindow", "ROI 4", nullptr));
        label_25->setText(QCoreApplication::translate("MainWindow", "y1:", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "Class lable", nullptr));
        good->setText(QCoreApplication::translate("MainWindow", "Good", nullptr));
        good->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "classLabel", nullptr)));
        good->setPressText(QCoreApplication::translate("MainWindow", "0", nullptr));
        good->setClickCheckedText(QCoreApplication::translate("MainWindow", "Good", nullptr));
        bad->setText(QCoreApplication::translate("MainWindow", "Bad", nullptr));
        bad->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "classLabel", nullptr)));
        bad->setClickCheckedText(QCoreApplication::translate("MainWindow", "Bad", nullptr));
        label_11->setText(QCoreApplication::translate("MainWindow", "extension", nullptr));
        extension->setProperty("variable", QVariant(QCoreApplication::translate("MainWindow", "extension", nullptr)));
        label_13->setText(QCoreApplication::translate("MainWindow", "Exp. time", nullptr));
        stream->setText(QCoreApplication::translate("MainWindow", "Stream", nullptr));
        stop->setText(QCoreApplication::translate("MainWindow", "Stop", nullptr));
        saveROI->setText(QCoreApplication::translate("MainWindow", "Save", nullptr));
        fileListing->setDirectoryPath(QCoreApplication::translate("MainWindow", "/home/control/AIProject/data", nullptr));
        qeimage->setProperty("imageVariable", QVariant(QString()));
        qeimage->setProperty("formatVariable", QVariant(QString()));
        qeimage->setProperty("widthVariable", QVariant(QString()));
        qeimage->setProperty("heightVariable", QVariant(QString()));
        qeimage->setProperty("regionOfInterest1XVariable", QVariant(QString()));
        qeimage->setProperty("regionOfInterest1YVariable", QVariant(QString()));
        qeimage->setProperty("regionOfInterest1WVariable", QVariant(QString()));
        qeimage->setProperty("regionOfInterest1HVariable", QVariant(QString()));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
