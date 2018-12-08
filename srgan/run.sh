for ((i=0;i<100;i++)); 
do
  python main.py --mode=evaluate --imid=$i;
done
