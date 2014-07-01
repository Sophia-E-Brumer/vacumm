"""Test the fortran function :f:func:`extrap1d`"""
from vcmq import N, P,meshcells, minmax, code_base_name
from vacumm.misc.grid.regridding import _extrap1d_


mv = 999.
vari = N.zeros((5,5))+mv
vari[1,2:4] = [2,3]
vari[2,1] = 1
vari[2,3] = 3
vari[3,3:] = [3,4]
vari[4,:2] = [0,1]
vari = N.asfortranarray(vari)

varo0 = _extrap1d_(vari, mv, 0)
varop1 = _extrap1d_(vari, mv, 1)
varom1 = _extrap1d_(vari, mv, -1)
varop2 = _extrap1d_(vari, mv, 2)

result = [
    ('AssertTrue', N.allclose(vari, varo0)), 
    ('AssertTrue', N.allclose(varop1[:, -1], [999., 3., 3., 4., 1.])), 
    ('AssertTrue', N.allclose(varom1[:, 0], [999., 2., 1., 3., 0.])), 
    ('AssertTrue', N.allclose(varop1[:, -1], varop2[:, -1])), 
    ('AssertTrue', N.allclose(varom1[:, 0], varop2[:, 0])), 
    ]
    
