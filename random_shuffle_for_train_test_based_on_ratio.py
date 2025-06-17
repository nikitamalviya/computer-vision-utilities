import os
import shutil
import random
from pathlib import Path

def split_dataset(source_folder, output_folder, train_ratio=0.8):
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

    # Shuffle and split
    random.shuffle(all_images)
    split_idx = int(len(all_images) * train_ratio)
    train_images = all_images[:split_idx]
    test_images = all_images[split_idx:]

    # Copy images
    for img in train_images:
        shutil.copy(img, train_path / img.name)
    for img in test_images:
        shutil.copy(img, test_path / img.name)

    print(f"Total images: {len(all_images)}")
    print(f"Train images: {len(train_images)} copied to {train_path}")
    print(f"Test images: {len(test_images)} copied to {test_path}")

# Example usage:
if __name__ == "__main__":
    source_folder = "path/to/your/image_folder"
    output_folder = "path/to/your/output_folder"
    train_ratio = 0.8  # Set this dynamically as needed (e.g., 0.7, 0.85)

    split_dataset(source_folder, output_folder, train_ratio)
