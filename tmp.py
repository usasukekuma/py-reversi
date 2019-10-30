
serializers.load_npz(npz_path, model1)
X1 = np.array(current_board, dtype=np.float32)
y1 = F.softmax(model1.predictor(X1))
tm1 = y1.data.argsort()
putting_list = [x1 for a1 in tm1 for x1 in a1]