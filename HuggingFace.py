from datasets import load_dataset, list_datasets,concatenate_datasets
def download_dataset_to_csv(dataset_name, output_dir='.'):
    """
    下载huggingface数据集并将其保存为CSV
    :param dataset_name: huggingface中的数据集名称
    :param output_dir: 输出文件夹
    """
    try:
        # 加载数据集
        dataset = load_dataset(dataset_name)

        # 将整个数据集合并为一个
        combined_dataset = concatenate_datasets([dataset[split] for split in dataset.keys()])

        # 将数据集保存为CSV
        output_path = f"{output_dir}/{dataset_name}.csv"
        combined_dataset.to_csv(output_path)
        print(f"Dataset {dataset_name} saved to: {output_path}")
    except Exception as e:
        print(f"Failed to download {dataset_name}. Error: {e}")

# 获取所有数据集的列表
all_datasets = list_datasets()

# 取前1500个数据集
datasets_to_download = all_datasets[:1500]

# 下载这1500个数据集
for ds in datasets_to_download:
    download_dataset_to_csv(ds)
