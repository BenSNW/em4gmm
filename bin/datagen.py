#!/usr/bin/env python3
import sys,random,math

# Write to disk the cache data and update the console message.
def write_cache(actual,samples,cache,file):
	file.write("\n".join(cache)+"\n")
	sys.stdout.write("\rGenerated sample "+str(actual)+" of "+str(samples)+".")
	return 0,[]

# Generate random Gaussian numbers based on the distributions.
def generate(samples,dimensions,distributions,file):
	file.write(str(dimensions)+" "+str(samples)+"\n")
	count,cache=0,[]
	for i in range(1,samples+1):
		distribution,numbers=random.choice(distributions),[]
		for j in range(dimensions):
			m,v=distribution[j]
			numbers.append(("%.3f"%random.gauss(m,v)))
		# Use a cache to speedup the write on disk.
		if count>=100000:
			count,cache=write_cache(i,samples,cache,file)
		else:
			count+=dimensions
			cache.append(" ".join(numbers))
	count,cache=write_cache(samples,samples,cache,file)
	sys.stdout.write("\n")

# Generate some random Gaussian distributions (mean and covariance).
def generate_distributions(samples,dimensions):
	numdist,distributions=int(math.sqrt(samples/2.0))+1,[]
	for i in range(numdist):
		distdim=[]
		for j in range(dimensions):
			m=random.uniform(-10000,10000)
			v=random.uniform(10,100)
			distdim.append((m,v))
		distributions.append(distdim)
	return distributions

# The main execution of the random data generator.
def main():
	if len(sys.argv)<4:
		sys.stderr.write("Usage: "+sys.argv[0]+" <dimensions> <samples> <file.txt>\n")
	else:
		dimensions=int(sys.argv[1])
		samples=int(sys.argv[2])
		file=open(str(sys.argv[3]),"w")
		distributions=generate_distributions(samples,dimensions)
		generate(samples,dimensions,distributions,file)
		file.close()

# If is not imported as a library, execute the main function.
if __name__=="__main__":
	main()
