from EmotionDetection import emotion_detector

def test_emotion(text, expected):
    result = emotion_detector(text)

    if result["dominant_emotion"] == expected:
        print("Passed")
    else:
        print("Failed")

test_emotion("I am glad this happened", "joy")
test_emotion("I am really mad about this", "anger")
test_emotion("I feel disgusted just hearing about this", "disgust")
test_emotion("I am so sad about this", "sadness")
test_emotion("I am really afraid that this will happen", "fear")