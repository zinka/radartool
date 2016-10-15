def rect(T):
    """create a centered rectangular pulse of width $T"""
    return lambda t: (t>=-T/2) & (t <= T/2)

def pulse_train(t, at, shape):
    """create a train of pulses over $t at times $at and shape $shape"""
    return np.sum(shape(t - at[:,np.newaxis]), axis=0)


    te = 1.5 # Expanded pulse width ... not required for Gaussian pulse
    
    wd = np.linspace(-20, 20, 100) # Doppler angular shift
    tau = 0 # Delay in time with respect to t0
    
    g1r = 'Gaussian(eta, te)[0]'
    g2r = 'Gaussian(eta+tau, te)[0]' 
    g1i = 'Gaussian(eta, te)[1]'
    g2i = 'Gaussian(eta+tau, te)[1]'    
    
    g1r = 'rect(eta, te)[0]'
    g2r = 'rect(eta+tau, te)[0]' 
    g1i = 'rect(eta, te)[1]'
    g2i = 'rect(eta+tau, te)[1]'     
    
    mu = 1
    g1r = 'LFM(eta, mu, te)[0]'
    g2r = 'LFM(eta+tau, mu, te)[0]' 
    g1i = 'LFM(eta, mu, te)[1]'
    g2i = 'LFM(eta+tau, mu, te)[1]'     
        
    ambig = np.array([])
    for i in wd:
        
        gg_real = lambda eta: (eval(g1r)*eval(g2r)+eval(g1i)*eval(g2i))*np.cos(i*eta)- (eval(g1r)*eval(g2i)-eval(g1i)*eval(g2r))*np.sin(i*eta)        
        tmp_real = integrate.quad(gg_real, -np.inf, np.inf)[0]
        
        gg_imag = lambda eta: (eval(g1r)*eval(g2r)+eval(g1i)*eval(g2i))*np.sin(i*eta)+ (eval(g1r)*eval(g2i)-eval(g1i)*eval(g2r))*np.cos(i*eta)        
        tmp_imag = integrate.quad(gg_imag, -np.inf, np.inf)[0]
        
        ambig = np.append(ambig, tmp_real+1j*tmp_imag) 
    
    plt.plot(wd, abs(ambig))
    plt.grid(True)
    plt.show() 
