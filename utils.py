from sklearn.datasets import fetch_openml

def load_mnist():
    mnist = fetch_openml('mnist_784',version=1)
    return mnist