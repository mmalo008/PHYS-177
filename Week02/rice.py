"""
Rice Question Program

Michael Malone
04/08/2016
"""
#global varibles
rice_weight=0.000015625
india_production=86.1*(10**9)

#calc
s=0
for i in range(64):
	s+=2**i

#output
print 'The game maker would receive ', s, 'grains of rice.'
print '\n'
print 'That is ', s*rice_weight, 'kg of rice, and would take India', (s*rice_weight)/india_production, 'years to produce.'
