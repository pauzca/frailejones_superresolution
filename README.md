
# Superresolución en Imágenes captadas por Dron para la Detección de Frailejones

La estructura del proyecto es:

```
/challenge
│
├── README.md             # Información sobre el proyecto 
├── .gitignore            # Archivos ignorados por Git 
├── requirements.txt      # Dependencias del proyecto 
├── /dataset               
    ├── /10_dic_2024_test_area_1cm         # Dataset de area de prueba
    ├── /10_dic_2024_test_area_3cm         # Dataset de area de prueba
    ├── /10_dic_2024_train_area_1cm        # Dataset de area de entrenamiento
├── /weights              # Pesos de los modelo Yolov11 (detección) y Real-ERSGAN 
├── /yaml_files           # Archivos yaml de configuración para el computo de métricas 📊
├── /yolo_cam             # Archivos del repositorio de YoloCam para Grad-Cam 
├── /Training_Real-ERSGAN.ipynb            # Entrenamiento de Real-ERSGAN
├── /inferencia_Superresolucion.ipynb      # Inferencia de imágenes del dataset de prueba con superresolución
├── /deteccion_superresolucion.ipynb       # Notebook con pruebas de deteccion
├── /reporte_escrito.pdf                   # Reporte escrito del proyecto
└── /rename_super_files.py                 # Script para renombrar archivos de inferencia con superresolucion 

```

Enlace a repositorio de github: https://github.com/pauzca/frailejones_superresolution
Enlace a google drive con el resto de los archivos que no subimos aqui: https://drive.google.com/drive/folders/1cwaX2VbHfEs48CPEInn4MqKlQrLeDKnl?usp=sharing
