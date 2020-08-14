if pgrep -f "paynpykeylogger.py" &>/dev/null; then
	echo "Process Started"

else 
	python3 closefile.py
fi