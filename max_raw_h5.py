"""Exploring a raw h5 file from a Maxwell device for some basic verification of its contents.  I may clean this up later."""

import h5py

with h5py.File('2023-04-02-e-hc328_unperturbed/original/data/hc3.28_hckcr1_chip16835_plated34.2_rec4.2.raw.h5', 'r') as f:
    print(f)
    #exit(0)
    print(f.keys())
    for k in f.keys():
        try:
            print(f'{f[k]}: {list(f[k].keys())}')
            for z in list(f[k].keys()):
                try:
                    print(f'{z}: {f[k][z][:]}')
                except:
                    print(f'{z}: {f[k][z]}')
                    #exit(0)
                    #print(f[k][z].keys())
                    #for y in list(f[k][z].keys()):
                    #    print(f[k][z][y][:])
                    #print(f'{z}: {f[k][z][:5, :5]}')
            #print(f[k].keys())
            #if 'gain' in list(f[k].keys()):
            #    print(f[k]['gain'][:])
            #print(f[k]['mapping'])
            #if 'mapping' in list(f[k].keys()):
            #    print('mapping')
            #    print(f[k]['mapping'][:])
            #if 'inputs' in list(f[k].keys()):
            #    print('inputs')
            #    print(f[k]['inputs'])
        except Exception as e:
            #print(e)
            try:
                print(f[k][:5, :5])
            except:
                print(f[k][:5])
        try:
            #print(f'fields: {f[k]} : {f[k].fields}')
            #print(dir(f[k]))
            #print(f[k][:5, :5])
            print(f'{f[k]}: {list(f[k].keys())}')
            for z in list(f[k].keys()):
                print(f'{z}: {f[k][z].data[:5]}')
        except:
            pass
    #print(min(data))
    #print(max(data))
    #print(data[:15])
