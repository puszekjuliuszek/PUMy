def foo_to_predict(x, sigma):
    foo = lambda x: 10*(((0.2*x-0.9)**5) - ((0.2*x-0.9)**3)  + ((0.2*x - 0.9)**2))
    return random.choice(np.random.normal(foo(x), sigma, 100))