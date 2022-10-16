OPERID="xx_xxxxxxxxxxxx_xxxxxxxxxxxx"
LOW_THRESHOLD=10
READING_LOG="elec.log"

get_reading() {
    PAYLOAD_STR=$(printf 'apistr={"operType":"BGRJ2018_CXDBSY_BY","operFlag":300023,"OperID":"%s"}' "$OPERID")
    FLOAT_VAL=$(curl -Gs http://www.cpcelc.pku.edu.cn/phone/socket.php \
        --data-urlencode "$PAYLOAD_STR" \
        | grep -oE "([0-9]{1,4}\.)[0-9]{1,3}" \
        | head -n 1)
    if [ -z "$FLOAT_VAL" ]; then
        echo "Failed to get reading"
        exit 1
    fi
    printf "%.0f" "$FLOAT_VAL"
}

get_date_iso() {
    date -u +"%Y-%m-%d %H:%M:%S"
}

READING=$(get_reading)
echo "Current reading: $READING"
echo "$(get_date_iso) $READING" >> "$READING_LOG"
