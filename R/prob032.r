
for(i in 12:98) {
	for(j in 123:987) {
		str1 <- paste(i, j, i*j, sep="")
		str2 <- strsplit(str1, "")
		sort(str2[[1]])
		if ( paste(sort(str2[[1]]), collapse="") == 123456789) {
			cat(i, j, i*j, "\n")
		}
	}
}


for(i in 1:9) {
	for(j in 1234:9876) {
		str1 <- paste(i, j, i*j, sep="")
		str2 <- strsplit(str1, "")
		sort(str2[[1]])
		if ( paste(sort(str2[[1]]), collapse="") == 123456789) {
			cat(i, j, i*j, "\n")
		}
	}
}

5796 + 5346 + 4396 + 7254 + 7632 + 6952 + 7852