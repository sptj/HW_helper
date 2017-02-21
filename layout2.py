/*
* The MIT License (MIT)
*
* Copyright : http://blog.csdn.net/liang19890820
*
* Author : 一去丶二三里
*
* Date : 2016/07/22
*
* Description : 黑色炫酷
*
*/

/**********子界面背景**********/
QWidget#customWidget {
        background: rgb(68, 69, 73);
}

/**********子界面中央背景**********/
QWidget#centerWidget {
        background: rgb(50, 50, 50);
}

/**********主界面样式**********/
QWidget#mainWindow {
        border: 1px solid rgb(50, 50, 50);
        background: rgb(50, 50, 50);
}

QWidget#messageWidget {
        background: rgba(68, 69, 73, 50%);
}

QWidget#loadingWidget {
        border: none;
        border-radius: 5px;
        background: rgb(50, 50, 50);
}

QWidget#remoteWidget {
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        border: 1px solid rgb(45, 45, 45);
        background: rgb(50, 50, 50);
}

StyledWidget {
        qproperty-normalColor: white;
        qproperty-disableColor: gray;
        qproperty-highlightColor: rgb(0, 160, 230);
        qproperty-errorColor: red;
}

QProgressIndicator {
        qproperty-color: rgb(175, 175, 175);
}

/**********提示**********/
QToolTip{
        border: 1px solid rgb(45, 45, 45);
        background: white;
        color: black;
}

/**********菜单栏**********/
QMenuBar {
        background: rgb(57, 58, 60);
        border: none;
}
QMenuBar::item {
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        color: rgb(227, 234, 242);
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        background: rgba(255, 255, 255, 40);
}

/**********菜单**********/
QMenu {
        border: 1px solid rgb(100, 100, 100);
        background: rgb(68, 69, 73);
}
QMenu::item {
        height: 22px;
        padding: 0px 25px 0px 20px;
}
QMenu::item:enabled {
        color: rgb(225, 225, 225);
}
QMenu::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenu::item:enabled:selected {
        color: rgb(230, 230, 230);
        background: rgba(255, 255, 255, 40);
}
QMenu::separator {
        height: 1px;
        background: rgb(100, 100, 100);
}
QMenu::indicator {
        width: 13px;
        height: 13px;
}
QMenu::icon {
        padding-left: 2px;
        padding-right: 2px;
}

/**********状态栏**********/
QStatusBar {
        background: rgb(57, 58, 60);
}
QStatusBar::item {
        border: none;
        border-right: 1px solid rgb(100, 100, 100);
}

/**********分组框**********/
QGroupBox {
        font-size: 15px;
        border: 1px solid rgb(80, 80, 80);
        border-radius: 4px;
        margin-top: 10px;
}
QGroupBox::title {
        color: rgb(175, 175, 175);
        top: -12px;
        left: 10px;
}

/**********页签项**********/
QTabWidget::pane {
        border: none;
        border-top: 3px solid rgb(0, 160, 230);
        background: rgb(57, 58, 60);
}
QTabWidget::tab-bar {
        border: none;
}
QTabBar::tab {
        border: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        color: rgb(175, 175, 175);
        background: rgb(255, 255, 255, 30);
        height: 28px;
        min-width: 85px;
        margin-right: 5px;
        padding-left: 5px;
        padding-right: 5px;
}
QTabBar::tab:hover {
        background: rgb(255, 255, 255, 40);
}
QTabBar::tab:selected {
        color: white;
        background: rgb(0, 160, 230);
}

QTabWidget#tabWidget::pane {
        border: 1px solid rgb(45, 45, 45);
        background: rgb(57, 58, 60);
        margin-top: -1px;
}

QTabBar#tabBar::tab {
        border: 1px solid rgb(45, 45, 45);
        border-bottom: none;
        background: transparent;
}
QTabBar#tabBar::tab:hover {
        color: white;
}
QTabBar#tabBar::tab:selected {
        color: white;
        background: rgb(57, 58, 60);
}

/**********表头**********/
QHeaderView{
        border: none;
        border-bottom: 3px solid rgb(0, 160, 230);
        background: rgb(57, 58, 60);
        min-height: 30px;
}
QHeaderView::section:horizontal {
        border: none;
        color: white;
        background: transparent;
        padding-left: 5px;
}
QHeaderView::section:horizontal:hover {
        background: rgb(0, 160, 230);
}
QHeaderView::section:horizontal:pressed {
        background: rgb(0, 180, 255);
}
QHeaderView::up-arrow {
        width: 13px;
        height: 11px;
        padding-right: 5px;
        image: url(:/Black/topArrow);
        subcontrol-position: center right;
}
QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {
        image: url(:/Black/topArrowHover);
}
QHeaderView::down-arrow {
        width: 13px;
        height: 11px;
        padding-right: 5px;
        image: url(:/Black/bottomArrow);
        subcontrol-position: center right;
}
QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {
        image: url(:/Black/bottomArrowHover);
}

/**********表格**********/
QTableView {
        border: 1px solid rgb(45, 45, 45);
        background: rgb(57, 58, 60);
        gridline-color: rgb(60, 60, 60);
}
QTableView::item {
        padding-left: 5px;
        padding-right: 5px;
        border: none;
        background: rgb(72, 72, 74);
        border-right: 1px solid rgb(45, 45, 45);
        border-bottom: 1px solid rgb(45, 45, 45);
}
QTableView::item:selected {
        background: rgba(255, 255, 255, 40);
}
QTableView::item:selected:!active {
        color: white;
}
QTableView::indicator {
        width: 20px;
        height: 20px;
}
QTableView::indicator:enabled:unchecked {
        image: url(:/Black/checkBox);
}
QTableView::indicator:enabled:unchecked:hover {
        image: url(:/Black/checkBoxHover);
}
QTableView::indicator:enabled:unchecked:pressed {
        image: url(:/Black/checkBoxPressed);
}
QTableView::indicator:enabled:checked {
        image: url(:/Black/checkBoxChecked);
}
QTableView::indicator:enabled:checked:hover {
        image: url(:/Black/checkBoxCheckedHover);
}
QTableView::indicator:enabled:checked:pressed {
        image: url(:/Black/checkBoxCheckedPressed);
}
QTableView::indicator:enabled:indeterminate {
        image: url(:/Black/checkBoxIndeterminate);
}
QTableView::indicator:enabled:indeterminate:hover {
        image: url(:/Black/checkBoxIndeterminateHover);
}
QTableView::indicator:enabled:indeterminate:pressed {
        image: url(:/Black/checkBoxIndeterminatePressed);
}

/**********滚动条-水平**********/
QScrollBar:horizontal {
        height: 20px;
        background: transparent;
        margin-top: 3px;
        margin-bottom: 3px;
}
QScrollBar::handle:horizontal {
        height: 20px;
        min-width: 30px;
        background: rgb(68, 69, 73);
        margin-left: 15px;
        margin-right: 15px;
}
QScrollBar::handle:horizontal:hover {
        background: rgb(80, 80, 80);
}
QScrollBar::sub-line:horizontal {
        width: 15px;
        background: transparent;
        image: url(:/Black/arrowLeft);
        subcontrol-position: left;
}
QScrollBar::add-line:horizontal {
        width: 15px;
        background: transparent;
        image: url(:/Black/arrowRight);
        subcontrol-position: right;
}
QScrollBar::sub-line:horizontal:hover {
        background: rgb(68, 69, 73);
}
QScrollBar::add-line:horizontal:hover {
        background: rgb(68, 69, 73);
}
QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
        background: transparent;
}

/**********滚动条-垂直**********/
QScrollBar:vertical {
        width: 20px;
        background: transparent;
        margin-left: 3px;
        margin-right: 3px;
}
QScrollBar::handle:vertical {
        width: 20px;
        min-height: 30px;
        background: rgb(68, 69, 73);
        margin-top: 15px;
        margin-bottom: 15px;
}
QScrollBar::handle:vertical:hover {
        background: rgb(80, 80, 80);
}
QScrollBar::sub-line:vertical {
        height: 15px;
        background: transparent;
        image: url(:/Black/arrowTop);
        subcontrol-position: top;
}
QScrollBar::add-line:vertical {
        height: 15px;
        background: transparent;
        image: url(:/Black/arrowBottom);
        subcontrol-position: bottom;
}
QScrollBar::sub-line:vertical:hover {
        background: rgb(68, 69, 73);
}
QScrollBar::add-line:vertical:hover {
        background: rgb(68, 69, 73);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: transparent;
}

QScrollBar#verticalScrollBar:vertical {
        margin-top: 30px;
}

/**********下拉列表**********/
QComboBox {
        height: 25px;
        border-radius: 4px;
        border: 1px solid rgb(100, 100, 100);
        background: rgb(72, 72, 73);
}
QComboBox:enabled {
        color: rgb(175, 175, 175);
}
QComboBox:!enabled {
        color: rgb(155, 155, 155);
}
QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(230, 230, 230);
        background: rgb(68, 69, 73);
}
QComboBox::drop-down {
        width: 20px;
        border: none;
        background: transparent;
}
QComboBox::drop-down:hover {
        background: rgba(255, 255, 255, 30);
}
QComboBox::down-arrow {
        image: url(:/Black/arrowBottom);
}
QComboBox::down-arrow:on {
        /**top: 1px;**/
}
QComboBox QAbstractItemView {
        border: 1px solid rgb(100, 100, 100);
        background: rgb(68, 69, 73);
        outline: none;
}
QComboBox QAbstractItemView::item {
        height: 25px;
        color: rgb(175, 175, 175);
}
QComboBox QAbstractItemView::item:selected {
        background: rgba(255, 255, 255, 40);
        color: rgb(230, 230, 230);
}

/**********进度条**********/
QProgressBar{
        border: none;
        text-align: center;
        color: white;
        background: rgb(48, 50, 51);
}
QProgressBar::chunk {
        background: rgb(0, 160, 230);
}

QProgressBar#progressBar {
        border: none;
        text-align: center;
        color: white;
        background-color: transparent;
        background-image: url(":/Black/progressBar");
        background-repeat: repeat-x;
}
QProgressBar#progressBar::chunk {
        border: none;
        background-color: transparent;
        background-image: url(":/Black/progressBarChunk");
        background-repeat: repeat-x;
}

/**********复选框**********/
QCheckBox{
        spacing: 5px;
}
QCheckBox:enabled{
        color: rgb(175, 175, 175);
}
QCheckBox:enabled:hover{
        color: rgb(200, 200, 200);
}
QCheckBox:!enabled{
        color: rgb(155, 155, 155);
}
QCheckBox::indicator {
        width: 20px;
        height: 20px;
}
QCheckBox::indicator:unchecked {
        image: url(:/Black/checkBox);
}
QCheckBox::indicator:unchecked:hover {
        image: url(:/Black/checkBoxHover);
}
QCheckBox::indicator:unchecked:pressed {
        image: url(:/Black/checkBoxPressed);
}
QCheckBox::indicator:checked {
        image: url(:/Black/checkBoxChecked);
}
QCheckBox::indicator:checked:hover {
        image: url(:/Black/checkBoxCheckedHover);
}
QCheckBox::indicator:checked:pressed {
        image: url(:/Black/checkBoxCheckedPressed);
}
QCheckBox::indicator:indeterminate {
        image: url(:/Black/checkBoxIndeterminate);
}
QCheckBox::indicator:indeterminate:hover {
        image: url(:/Black/checkBoxIndeterminateHover);
}
QCheckBox::indicator:indeterminate:pressed {
        image: url(:/Black/checkBoxIndeterminatePressed);
}

/**********单选框**********/
QRadioButton{
        spacing: 5px;
}
QRadioButton:enabled{
        color: rgb(175, 175, 175);
}
QRadioButton:enabled:hover{
        color: rgb(200, 200, 200);
}
QRadioButton:!enabled{
        color: rgb(155, 155, 155);
}
QRadioButton::indicator {
        width: 20px;
        height: 20px;
}
QRadioButton::indicator:unchecked {
        image: url(:/Black/radioButton);
}
QRadioButton::indicator:unchecked:hover {
        image: url(:/Black/radioButtonHover);
}
QRadioButton::indicator:unchecked:pressed {
        image: url(:/Black/radioButtonPressed);
}
QRadioButton::indicator:checked {
        image: url(:/Black/radioButtonChecked);
}
QRadioButton::indicator:checked:hover {
        image: url(:/Black/radioButtonCheckedHover);
}
QRadioButton::indicator:checked:pressed {
        image: url(:/Black/radioButtonCheckedPressed);
}

/**********输入框**********/
QLineEdit {
        border-radius: 4px;
        height: 25px;
        border: 1px solid rgb(100, 100, 100);
        background: rgb(72, 72, 73);
}
QLineEdit:enabled {
        color: rgb(175, 175, 175);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(230, 230, 230);
}
QLineEdit:!enabled {
        color: rgb(155, 155, 155);
}

/**********文本编辑框**********/
QTextEdit {
        border: 1px solid rgb(45, 45, 45);
        color: rgb(175, 175, 175);
        background: rgb(57, 58, 60);
}

/**********滚动区域**********/
QScrollArea {
        border: 1px solid rgb(45, 45, 45);
        background: rgb(57, 58, 60);
}

/**********滚动区域**********/
QWidget#transparentWidget {
        background: transparent;
}

/**********微调器**********/
QSpinBox {
        border-radius: 4px;
        height: 24px;
        min-width: 40px;
        border: 1px solid rgb(100, 100, 100);
        background: rgb(68, 69, 73);
}
QSpinBox:enabled {
        color: rgb(220, 220, 220);
}
QSpinBox:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(230, 230, 230);
}
QSpinBox:!enabled {
        color: rgb(65, 65, 65);
        background: transparent;
}
QSpinBox::up-button {
        width: 18px;
        height: 12px;
        border-top-right-radius: 4px;
        border-left: 1px solid rgb(100, 100, 100);
        image: url(:/Black/upButton);
        background: rgb(50, 50, 50);
}
QSpinBox::up-button:!enabled {
        border-left: 1px solid gray;
        background: transparent;
}
QSpinBox::up-button:enabled:hover {
        background: rgb(255, 255, 255, 30);
}
QSpinBox::down-button {
        width: 18px;
        height: 12px;
        border-bottom-right-radius: 4px;
        border-left: 1px solid rgb(100, 100, 100);
        image: url(:/Black/downButton);
        background: rgb(50, 50, 50);
}
QSpinBox::down-button:!enabled {
        border-left: 1px solid gray;
        background: transparent;
}
QSpinBox::down-button:enabled:hover {
        background: rgb(255, 255, 255, 30);
}

/**********标签**********/
QLabel#grayLabel {
        color: rgb(175, 175, 175);
}

QLabel#highlightLabel {
        color: rgb(175, 175, 175);
}

QLabel#redLabel {
        color: red;
}

QLabel#grayYaHeiLabel {
        color: rgb(175, 175, 175);
        font-size: 16px;
}

QLabel#blueLabel {
        color: rgb(0, 160, 230);
}

QLabel#listLabel {
        color: rgb(0, 160, 230);
}

QLabel#lineBlueLabel {
        background: rgb(0, 160, 230);
}

QLabel#graySeperateLabel {
        background: rgb(45, 45, 45);
}

QLabel#seperateLabel {
        background: rgb(80, 80, 80);
}

QLabel#radiusBlueLabel {
        border-radius: 15px;
        color: white;
        font-size: 16px;
        background: rgb(0, 160, 230);
}

QLabel#skinLabel[colorProperty="normal"] {
        color: rgb(175, 175, 175);
}
QLabel#skinLabel[colorProperty="highlight"] {
        color: rgb(0, 160, 230);
}

QLabel#informationLabel {
        qproperty-pixmap: url(:/Black/information);
}

QLabel#errorLabel {
        qproperty-pixmap: url(:/Black/error);
}

QLabel#successLabel {
        qproperty-pixmap: url(:/Black/success);
}

QLabel#questionLabel {
        qproperty-pixmap: url(:/Black/question);
}

QLabel#warningLabel {
        qproperty-pixmap: url(:/Black/warning);
}

QLabel#groupLabel {
        color: rgb(0, 160, 230);
        border: 1px solid rgb(0, 160, 230);
        font-size: 15px;
        border-top-color: transparent;
        border-right-color: transparent;
        border-left-color: transparent;
}

/**********按钮**********/
QToolButton#nsccButton{
        border: none;
        color: rgb(175, 175, 175);
        background: transparent;
        padding: 10px;
        qproperty-icon: url(:/Black/nscc);
        qproperty-iconSize: 32px 32px;
        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;
}
QToolButton#nsccButton:hover{
        color: rgb(217, 218, 218);
        background: rgb(255, 255, 255, 20);
}

QToolButton#transferButton{
        border: none;
        color: rgb(175, 175, 175);
        background: transparent;
        padding: 10px;
        qproperty-icon: url(:/Black/transfer);
        qproperty-iconSize: 32px 32px;
        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;
}
QToolButton#transferButton:hover{
        color: rgb(217, 218, 218);
        background: rgb(255, 255, 255, 20);
}

/**********按钮**********/
QPushButton{
        border-radius: 4px;
        border: none;
        width: 75px;
        height: 25px;
}
QPushButton:enabled {
        background: rgb(68, 69, 73);
        color: white;
}
QPushButton:!enabled {
        background: rgb(100, 100, 100);
        color: rgb(200, 200, 200);
}
QPushButton:enabled:hover{
        background: rgb(85, 85, 85);
}
QPushButton:enabled:pressed{
        background: rgb(80, 80, 80);
}

QPushButton#blueButton {
        color: white;
}
QPushButton#blueButton:enabled {
        background: rgb(0, 165, 235);
        color: white;
}
QPushButton#blueButton:!enabled {
        background: gray;
        color: rgb(200, 200, 200);
}
QPushButton#blueButton:enabled:hover {
        background: rgb(0, 180, 255);
}
QPushButton#blueButton:enabled:pressed {
        background: rgb(0, 140, 215);
}

QPushButton#selectButton {
        border: none;
        border-radius: none;
        border-left: 1px solid rgb(100, 100, 100);
        image: url(:/Black/scan);
        background: transparent;
        color: white;
}
QPushButton#selectButton:enabled:hover{
        background: rgb(85, 85, 85);
}
QPushButton#selectButton:enabled:pressed{
        background: rgb(80, 80, 80);
}

QPushButton#linkButton {
        background: transparent;
        color: rgb(0, 160, 230);
        text-align:left;
}
QPushButton#linkButton:hover {
        color: rgb(20, 185, 255);
        text-decoration: underline;
}
QPushButton#linkButton:pressed {
        color: rgb(0, 160, 230);
}

QPushButton#transparentButton {
        background: transparent;
}

/*****************标题栏按钮*******************/
QPushButton#minimizeButton {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/minimize);
}
QPushButton#minimizeButton:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/minimizeHover);
}
QPushButton#minimizeButton:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/minimizePressed);
}

QPushButton#maximizeButton[maximizeProperty="maximize"] {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/maximize);
}
QPushButton#maximizeButton[maximizeProperty="maximize"]:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/maximizeHover);
}
QPushButton#maximizeButton[maximizeProperty="maximize"]:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/maximizePressed);
}

QPushButton#maximizeButton[maximizeProperty="restore"] {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/restore);
}
QPushButton#maximizeButton[maximizeProperty="restore"]:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/restoreHover);
}
QPushButton#maximizeButton[maximizeProperty="restore"]:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/restorePressed);
}

QPushButton#closeButton {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/close);
}
QPushButton#closeButton:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/closeHover);
}
QPushButton#closeButton:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/closePressed);
}

QPushButton#skinButton {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/skin);
}
QPushButton#skinButton:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/skinHover);
}
QPushButton#skinButton:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/skinPressed);
}

QPushButton#feedbackButton {
        border-radius: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        background: rgb(50, 50, 50);
        image: url(:/Black/feedback);
}
QPushButton#feedbackButton:hover {
        background: rgb(60, 60, 60);
        image: url(:/Black/feedbackHover);
}
QPushButton#feedbackButton:pressed {
        background: rgb(55, 55, 55);
        image: url(:/Black/feedbackPressed);
}

QPushButton#closeTipButton {
        border-radius: none;
        border-image: url(:/Black/close);
        background: transparent;
}
QPushButton#closeTipButton:hover {
        border-image: url(:/Black/closeHover);
}
QPushButton#closeTipButton:pressed {
        border-image: url(:/Black/closePressed);
}

QPushButton#changeSkinButton{
        border-radius: 4px;
        border: 2px solid rgb(41, 41, 41);
        background: rgb(51, 51, 51);
}
QPushButton#changeSkinButton:hover{
        border-color: rgb(45, 45, 45);
}
QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{
        border-color: rgb(0, 160, 230);
}

QPushButton#transferButton {
        padding-left: 5px;
        padding-right: 5px;
        color: white;
        background: rgb(0, 165, 235);
}
QPushButton#transferButton:hover {
        background: rgb(0, 180, 255);
}
QPushButton#transferButton:pressed {
        background: rgb(0, 140, 215);
}
QPushButton#transferButton[iconProperty="left"] {
        qproperty-icon: url(:/Black/left);
}
QPushButton#transferButton[iconProperty="right"] {
        qproperty-icon: url(:/Black/right);
}

QPushButton#openButton {
        border-radius: none;
        image: url(:/Black/open);
        background: transparent;
}
QPushButton#openButton:hover {
        image: url(:/Black/openHover);
}
QPushButton#openButton:pressed {
        image: url(:/Black/openPressed);
}

QPushButton#deleteButton {
        border-radius: none;
        image: url(:/Black/delete);
        background: transparent;
}
QPushButton#deleteButton:hover {
        image: url(:/Black/deleteHover);
}
QPushButton#deleteButton:pressed {
        image: url(:/Black/deletePressed);
}

QPushButton#menuButton {
        text-align: left center;
        padding-left: 3px;
        color: rgb(175, 175, 175);
        border: 1px solid rgb(100, 100, 100);
        background: rgb(72, 72, 73);
}
QPushButton#menuButton::menu-indicator{
        subcontrol-position: right center;
        subcontrol-origin: padding;
        image: url(:/Black/arrowBottom);
        padding-right: 3px;
}