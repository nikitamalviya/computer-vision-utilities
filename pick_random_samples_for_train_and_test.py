import os
import shutil
import random
from pathlib import Path

def split_dataset_by_count(source_folder, output_folder, train_count, test_count):
    source_path = Path(source_folder)
    output_path = Path(output_folder)

    # Create train and test directories
    train_path = output_path / 'train'
    test_path = output_path / 'test'
    train_path.mkdir(parents=True, exist_ok=True)
    test_path.mkdir(parents=True, exist_ok=True)

    # Get all image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']
    all_images = [f for f in source_path.iterdir() if f.suffix.lower() in image_extensions]

    # Check if enough images exist
    total_required = train_count + test_count
    if len(all_images) < total_required:
        raise ValueError(f"Not enough images in source folder. Required: {total_required}, Found: {len(all_images)}")

    # Shuffle and sample
    random.shuffle(all_images)
    train_images = all_images[:train_count]
    test_images = all_images[train_count:train_count + test_count]

    # Copy images
    for img in train_images:
        shutil.copy(img, train_path / img.name)
    for img in test_images:
        shutil.copy(img, test_path / img.name)

    print(f"Train images: {len(train_images)} copied to {train_path}")
    print(f"Test images: {len(test_images)} copied to {test_path}")

# Example usage:
if __name__ == "__main__":
    source_folder = "path/to/your/image_folder"
    output_folder = "path/to/your/output_folder"
    train_count = 200  # Number of training samples
    test_count = 50    # Number of test samples

    split_dataset_by_count(source_folder, output_folder, train_count, test_count)
