# Run the baseline
python baseline.py dev-0
python baseline.py test-A
python baseline.py test-B

# Evaluate the baseline results on the dev-0 dataset
wget https://gonito.net/get/bin/geval
chmod u+x geval
echo $(./geval -t dev-0)
