def predictions_with_classification_report(model, generator, y_true):
    # Making Predictions on Test Data
    y_preds = model.predict(generator)
    y_preds = np.argmax(y_preds, axis=1)

    #Classification Report: 
    print("classification Report:")
    print(classification_report(y_true, y_preds))
    return y_preds

def plot_history(history):
    
    # summarize history for accuracy
    plt.figure(figsize=(18,6))
    
    plt.subplot(121)
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.ylim((0,1))    
    
    # summarize history for loss
    plt.subplot(122)
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

def plot_confusion_matrix(y_true, y_preds):
    
    # Confusion Matrix

    fig=plt.figure()
    fig.set_size_inches(18,8)

    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    
    class_names_list = ['human', 'noise', 'animal', 'music', 'ambient', 'alarm', 'movement', 'other']
    
    sns.heatmap(confusion_matrix(y_true, y_preds, normalize=None),
                annot=True, fmt='g', cmap='Blues', cbar=False, ax=ax1)

    ax1.set_xlabel("Predicted labels")
    ax1.set_ylabel("True labels")
    ax1.set_title('Confusion matrix ')
    ax1.set_xticklabels(class_names_list)
    ax1.set_yticklabels(class_names_list, rotation='horizontal')

    sns.heatmap(confusion_matrix(y_true, y_preds, normalize='true'),  
                annot=True, fmt='g', cmap='Blues', cbar=False, ax=ax2)
    ax2.set_xlabel("Predicted labels")
    ax2.set_ylabel("True labels")
    ax2.set_title('Confusion matrix (Normalized by True Labels)')
    ax2.set_xticklabels(class_names_list)
    ax2.set_yticklabels(class_names_list, rotation='horizontal')    
    plt.show() 
    
def plot_five(dataframe):
    plt.figure(figsize=(20,4))
    for idx,i in enumerate(dataframe.png_name):
        plt.subplot(1,5,idx+1)
        img = mpimg.imread('data/test_spectrograms/' + i)
        imgplot = plt.imshow(img, origin='lower')
        plt.title("Spectrogram " + dataframe.iloc[idx]['png_name'])
    plt.show()    