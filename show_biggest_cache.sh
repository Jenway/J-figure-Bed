function get_biggest_files() {
    # return the 20 biggest files's hash and size
    git verify-pack -v .git/objects/pack/pack-*.idx | sort -k 3 -n | tail -50 | awk '{print $1" "$3}'
}

function get_file_name() {
    git rev-list --objects --all | grep $1 | awk '{print $2}'
}


echo "Getting biggest files"
var=$(get_biggest_files)
echo "Done"
echo "Getting file name"

echo "$var" | while read i j; do
    # 取哈希值的前六位
    i=$(echo "$i" | cut -c 1-6)
    # 换算文件大小
    j=$(awk "BEGIN {printf \"%.2f\", $j / 1024 / 1024}")
    echo "$i : $(get_file_name "$i") $j KB"
done