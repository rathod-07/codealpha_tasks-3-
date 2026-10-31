import os
import shutil


def organize_jpg_files(folder_path):
	"""Move .jpg and .jpeg files from folder_path into its Images folder."""
	print("=" * 52)
	print(" IMAGE FILE ORGANIZER")
	print("Target folder: " + folder_path)
	print("=" * 52)

	if not os.path.isdir(folder_path):
		print(" Error: The folder does not exist.")
		return

	images_folder = os.path.join(folder_path, "Images")
	os.makedirs(images_folder, exist_ok=True)

	moved_count = 0
	skipped_count = 0
	matched_count = 0

	# Only inspect files directly inside the selected folder.
	for filename in os.listdir(folder_path):
		source_path = os.path.join(folder_path, filename)

		# Ignore folders and match extensions without regard to letter case.
		if os.path.isfile(source_path) and filename.lower().endswith((".jpg", ".jpeg")):
			matched_count += 1
			destination_path = os.path.join(images_folder, filename)

			# Avoid overwriting an image already in the destination folder.
			if os.path.exists(destination_path):
				print(" Skipped (already exists): " + filename)
				skipped_count += 1
				continue

			shutil.move(source_path, destination_path)
			print(" Moved: " + filename + " → Images")
			moved_count += 1

	if matched_count == 0:
		print(" No .jpg or .jpeg files found in this folder.")

	print("-" * 52)
	print(" Organization complete")
	print("Moved: " + str(moved_count) + " | Skipped: " + str(skipped_count))
	print("=" * 52)


if __name__ == "__main__":
	# Set this to the folder you want to organize, or enter its path when asked.
	target_folder = input(
		"Folder to organize (press Enter for this script's folder): "
	).strip()
	if not target_folder:
		target_folder = os.path.dirname(os.path.abspath(__file__))

	organize_jpg_files(target_folder)
