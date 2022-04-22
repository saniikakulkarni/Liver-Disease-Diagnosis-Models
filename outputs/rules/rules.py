def findDecision(obj): #obj[0]: Age, obj[1]: Gender, obj[2]: TB, obj[3]: DB, obj[4]: AP, obj[5]: SGPT, obj[6]: SGOT, obj[7]: TP, obj[8]: ALB, obj[9]: A/G
	# {"feature": "DB", "instances": 624, "metric_value": 0.0484, "depth": 1}
	if obj[3]<=1.2416666666666705:
		# {"feature": "SGPT", "instances": 500, "metric_value": 0.0228, "depth": 2}
		if obj[5]<=4.19947494879193:
			# {"feature": "AP", "instances": 438, "metric_value": 0.0143, "depth": 3}
			if obj[4]<=6.405404874345977:
				# {"feature": "Age", "instances": 429, "metric_value": 0.0035, "depth": 4}
				if obj[0]<=43.61072261072261:
					# {"feature": "SGOT", "instances": 218, "metric_value": 0.0072, "depth": 5}
					if obj[6]<=109.44036181257141:
						# {"feature": "TB", "instances": 213, "metric_value": 0.0086, "depth": 6}
						if obj[2]<=0.8754687373538999:
							# {"feature": "A/G", "instances": 188, "metric_value": 0.0047, "depth": 7}
							if obj[9]>0.4054651081081644:
								# {"feature": "TP", "instances": 185, "metric_value": 0.0046, "depth": 8}
								if obj[7]>2.8:
									# {"feature": "ALB", "instances": 184, "metric_value": 0.0047, "depth": 9}
									if obj[8]<=4.995752825932845:
										# {"feature": "Gender", "instances": 183, "metric_value": 0.0012, "depth": 10}
										if obj[1]>0.0:
											return 2.0
										elif obj[1]<=0.0:
											return 2.0
										else: return 1.7096774193548387
									elif obj[8]>4.995752825932845:
										return 1.0
									else: return 1.0
								elif obj[7]<=2.8:
									return 1.0
								else: return 1.0
							elif obj[9]<=0.4054651081081644:
								return 2.0
							else: return 2.0
						elif obj[2]>0.8754687373538999:
							# {"feature": "A/G", "instances": 25, "metric_value": 0.133, "depth": 7}
							if obj[9]<=0.6931471805599453:
								# {"feature": "ALB", "instances": 19, "metric_value": 0.1177, "depth": 8}
								if obj[8]>2.7:
									# {"feature": "Gender", "instances": 16, "metric_value": 0.1268, "depth": 9}
									if obj[1]>0.0:
										# {"feature": "TP", "instances": 10, "metric_value": 0.1435, "depth": 10}
										if obj[7]<=8.0:
											return 1.0
										elif obj[7]>8.0:
											return 2.0
										else: return 2.0
									elif obj[1]<=0.0:
										return 2.0
									else: return 2.0
								elif obj[8]<=2.7:
									return 1.0
								else: return 1.0
							elif obj[9]>0.6931471805599453:
								return 1.0
							else: return 1.0
						else: return 1.48
					elif obj[6]>109.44036181257141:
						return 2.0
					else: return 2.0
				elif obj[0]>43.61072261072261:
					# {"feature": "TB", "instances": 211, "metric_value": 0.009, "depth": 5}
					if obj[2]<=1.23194934088297:
						# {"feature": "SGOT", "instances": 208, "metric_value": 0.0076, "depth": 6}
						if obj[6]>12.0:
							# {"feature": "TP", "instances": 204, "metric_value": 0.0062, "depth": 7}
							if obj[7]<=8.476089341152846:
								# {"feature": "ALB", "instances": 202, "metric_value": 0.0078, "depth": 8}
								if obj[8]<=4.67596423136572:
									# {"feature": "Gender", "instances": 198, "metric_value": 0.0044, "depth": 9}
									if obj[1]>0.0:
										# {"feature": "A/G", "instances": 137, "metric_value": 0.0274, "depth": 10}
										if obj[9]<=0.6985993866630054:
											return 1.0
										elif obj[9]>0.6985993866630054:
											return 2.0
										else: return 1.75
									elif obj[1]<=0.0:
										# {"feature": "A/G", "instances": 61, "metric_value": 0.0397, "depth": 10}
										if obj[9]<=0.832909122935104:
											return 2.0
										elif obj[9]>0.832909122935104:
											return 1.0
										else: return 1.0
									else: return 1.7049180327868851
								elif obj[8]>4.67596423136572:
									return 2.0
								else: return 2.0
							elif obj[7]>8.476089341152846:
								return 1.0
							else: return 1.0
						elif obj[6]<=12.0:
							return 2.0
						else: return 2.0
					elif obj[2]>1.23194934088297:
						return 1.0
					else: return 1.0
				else: return 1.6113744075829384
			elif obj[4]>6.405404874345977:
				return 1.0
			else: return 1.0
		elif obj[5]>4.19947494879193:
			# {"feature": "Age", "instances": 62, "metric_value": 0.0569, "depth": 3}
			if obj[0]<=38.435483870967744:
				# {"feature": "ALB", "instances": 35, "metric_value": 0.0764, "depth": 4}
				if obj[8]<=3.9:
					# {"feature": "TB", "instances": 28, "metric_value": 0.0753, "depth": 5}
					if obj[2]<=1.1631508098056809:
						# {"feature": "AP", "instances": 26, "metric_value": 0.1804, "depth": 6}
						if obj[4]>5.214935757608986:
							# {"feature": "SGOT", "instances": 23, "metric_value": 0.1067, "depth": 7}
							if obj[6]<=188.30434782608697:
								return 1.0
							elif obj[6]>188.30434782608697:
								# {"feature": "A/G", "instances": 6, "metric_value": 0.206, "depth": 8}
								if obj[9]>0.6418538861723948:
									return 1.0
								elif obj[9]<=0.6418538861723948:
									return 1.5
								else: return 1.5
							else: return 1.1666666666666667
						elif obj[4]<=5.214935757608986:
							return 2.0
						else: return 2.0
					elif obj[2]>1.1631508098056809:
						return 2.0
					else: return 2.0
				elif obj[8]>3.9:
					# {"feature": "SGOT", "instances": 7, "metric_value": 0.3499, "depth": 5}
					if obj[6]<=90.0:
						return 2.0
					elif obj[6]>90.0:
						return 1.0
					else: return 1.0
				else: return 1.8571428571428572
			elif obj[0]>38.435483870967744:
				# {"feature": "TP", "instances": 27, "metric_value": 0.1148, "depth": 4}
				if obj[7]<=7.790508940207399:
					return 1.0
				elif obj[7]>7.790508940207399:
					# {"feature": "SGOT", "instances": 5, "metric_value": 0.4, "depth": 5}
					if obj[6]>74.0:
						return 1.0
					elif obj[6]<=74.0:
						return 2.0
					else: return 2.0
				else: return 1.2
			else: return 1.037037037037037
		else: return 1.2096774193548387
	elif obj[3]>1.2416666666666705:
		# {"feature": "Age", "instances": 124, "metric_value": 0.0411, "depth": 2}
		if obj[0]<=59.90224229230624:
			# {"feature": "TB", "instances": 95, "metric_value": 0.0876, "depth": 3}
			if obj[2]<=2.131667079824185:
				# {"feature": "A/G", "instances": 57, "metric_value": 0.0481, "depth": 4}
				if obj[9]>0.41871033485818504:
					# {"feature": "AP", "instances": 47, "metric_value": 0.0602, "depth": 5}
					if obj[4]>5.11677887252395:
						# {"feature": "ALB", "instances": 41, "metric_value": 0.0783, "depth": 6}
						if obj[8]>2.3:
							# {"feature": "SGPT", "instances": 32, "metric_value": 0.2421, "depth": 7}
							if obj[5]>2.4849066497880004:
								return 1.0
							elif obj[5]<=2.4849066497880004:
								return 2.0
							else: return 2.0
						elif obj[8]<=2.3:
							# {"feature": "SGOT", "instances": 9, "metric_value": 0.2747, "depth": 7}
							if obj[6]>64.0:
								# {"feature": "SGPT", "instances": 5, "metric_value": 0.2, "depth": 8}
								if obj[5]<=4.060443010546419:
									return 1.0
								elif obj[5]>4.060443010546419:
									return 1.5
								else: return 1.5
							elif obj[6]<=64.0:
								return 2.0
							else: return 2.0
						else: return 1.5555555555555556
					elif obj[4]<=5.11677887252395:
						# {"feature": "SGPT", "instances": 6, "metric_value": 0.3727, "depth": 6}
						if obj[5]<=3.4965075614664802:
							return 2.0
						elif obj[5]>3.4965075614664802:
							return 1.0
						else: return 1.0
					else: return 1.8333333333333333
				elif obj[9]<=0.41871033485818504:
					return 1.0
				else: return 1.0
			elif obj[2]>2.131667079824185:
				return 1.0
			else: return 1.0
		elif obj[0]>59.90224229230624:
			return 1.0
		else: return 1.0
	else: return 1.096774193548387
