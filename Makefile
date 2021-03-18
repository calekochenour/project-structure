# Set phony targets
.PHONY: create clean

# Create folder structure
create: create-folders.py
	python create-folders.py

# Delete folder structure
clean:
	rm -rf 01-code-scripts
	rm -rf 02-raw-data
	rm -rf 03-processed-data
	rm -rf 04-graphics-outputs
	rm -rf 05-papers-writings
