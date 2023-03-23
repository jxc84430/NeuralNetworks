Spring 2023 : CS5720 Neural Networks & Deep Learning

Name : Jahnavi Chadalavada

ID : 700728443

Summary of ICP_7:

This Assignment is on Image Classification with CNN using keras.

1. Follow the instruction below and then report how the performance changed.(apply all at once)
• Convolutional input layer, 32 feature maps with a size of 3×3 and a rectifier activation function.
• Dropout layer at 20%.
• Convolutional layer, 32 feature maps with a size of 3×3 and a rectifier activation function.
• Max Pool layer with size 2×2.
• Convolutional layer, 64 feature maps with a size of 3×3 and a rectifier activation function.
• Dropout layer at 20%.
• Convolutional layer, 64 feature maps with a size of 3×3 and a rectifier activation function.
• Max Pool layer with size 2×2.
• Convolutional layer, 128 feature maps with a size of 3×3 and a rectifier activation function.
• Dropout layer at 20%.
• Convolutional layer,128 feature maps with a size of 3×3 and a rectifier activation function.
• Max Pool layer with size 2×2.
• Flatten layer.
• Dropout layer at 20%.
• Fully connected layer with 1024 units and a rectifier activation function.
• Dropout layer at 20%.
• Fully connected layer with 512 units and a rectifier activation function.
• Dropout layer at 20%.
• Fully connected output layer with 10 units and a Softmax activation function

      Model Accuracy has reduced from 90% to 87% where as validation accuracy improved from 69% to 79%.Execution time Increased.Model predicted first four test images correctly with these changes where as previous code predicted one image incorrectly.

2. Predict the first 4 images of the test data using the above model. Then, compare with the actual label for those 4 images to check whether or not the model has predicted correctly.
   
     Model has predicted correctly first 4 images.
   
3. Visualize Loss and Accuracy using the history object

      Plotted the graph using matplotlib
      
Video Link : https://drive.google.com/file/d/1OI_zXMdmyp7a5clz3E9LPAXzKxU7Htqd/view?usp=sharing
