import pickle
from keras.preprocessing import sequence
from keras.models import load_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prediction
from .serializers import PredictionSerializer


class PredictionAPIView(APIView):
    def get(self, request):
        text = self.request.query_params.get('text', None)
        if text is not None:
            with open('./ml_models/dodo_tokenizer.pickle', 'rb') as f:
                tokenizer = pickle.load(f)
            model = load_model('./ml_models/dodo_cnn_sentiment.hdf5')
            score = self.evaluate_score(text, model, tokenizer)
            class_ind = 1 if score > 0.5 else 0
            predictions = Prediction(text=text, class_ind=class_ind)
            serializer = PredictionSerializer(predictions)
        else:
            predictions = Prediction.objects.all()
            serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)

    def evaluate_score(self, text, model, tokenizer):
        phrases = [text]
        checks = tokenizer.texts_to_sequences(phrases)
        checks = sequence.pad_sequences(checks, maxlen=150)
        answers = model.predict(checks, batch_size=64)
        return answers[0][0]
