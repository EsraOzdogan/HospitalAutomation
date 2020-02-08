def insertion_sort(dizi: list):
    for j in range(1, len(dizi)):
        guncel = dizi[j]
        i=j-1
        while i >= 0 and dizi[i] > guncel:
            dizi[i+1]=dizi[i]
            i = i-1
        dizi[i+1] = guncel
    return dizi
if __name__=="__main__":
    dizi = ["b", "h", "a", "k", "c", "y"]
    dizi = insertion_sort(dizi)
    for i in dizi:
        print(i)
