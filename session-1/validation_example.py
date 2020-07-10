import ostap.fitting.models
import ostap.fitting.toys
x = ROOT.RooRealVar(’x’, ’x’, -1, 1)
model = ostap.fitting.models.Gauss_pdf(’G’, x,mean = (0, -1, 1), sigma = (.1, .001, 5))
result, stats = ostap.fitting.toys.make_toys(model, 1000, [x],
    gen_config = {’nEvents’:  1000},
    init_pars = {’mean_G’: .2, ’sigma_G’: .2})
h = ROOT.TH1D(’h’, ’h’, 1000, stats[’mean_G’].min(),stats[’mean_G’].max())
for i in result[’mean_G’]:
    h.Fill(i.value())

h.Draw() # see is it gaussian# compare stats[’par’].mean() and stats[’par’].rms() with exp.fit result
