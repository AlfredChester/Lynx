while true; do
./mk > tmp.in
./1 < tmp.in > 1.out
./2 < tmp.in > 2.out
if diff 1.out 2.out; then
echo AC
else
echo WA
exit 0
fi
done
