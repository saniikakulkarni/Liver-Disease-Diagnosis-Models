def findDecision(obj): #obj[0]: Age, obj[1]: Gender, obj[2]: TB, obj[3]: DB, obj[4]: AP, obj[5]: SGPT, obj[6]: SGOT, obj[7]: TP, obj[8]: ALB, obj[9]: A/G
	# {"feature": "DB", "instances": 466, "metric_value": 0.0453, "depth": 1}
	if obj[3]<=1.4358369098712498:
		# {"feature": "SGOT", "instances": 368, "metric_value": 0.0136, "depth": 2}
		if obj[6]<=232.0438043817474:
			# {"feature": "AP", "instances": 355, "metric_value": 0.0112, "depth": 3}
			if obj[4]<=726.6886187856755:
				# {"feature": "TB", "instances": 345, "metric_value": 0.0095, "depth": 4}
				if obj[2]<=1.7195653403005178:
					# {"feature": "SGPT", "instances": 288, "metric_value": 0.0109, "depth": 5}
					if obj[5]<=68.47035291170018:
						# {"feature": "Age", "instances": 264, "metric_value": 0.0081, "depth": 6}
						if obj[0]>27.59263559282497:
							# {"feature": "TP", "instances": 218, "metric_value": 0.0078, "depth": 7}
							if obj[7]>4.439355642516821:
								# {"feature": "ALB", "instances": 214, "metric_value": 0.0082, "depth": 8}
								if obj[8]>1.8070136102120924:
									# {"feature": "A/G", "instances": 211, "metric_value": 0.003, "depth": 9}
									if obj[9]<=1.0127488151658772:
										# {"feature": "Gender", "instances": 140, "metric_value": 0.0032, "depth": 10}
										if obj[1]>0.0:
											return 1.0
										elif obj[1]<=0.0:
											return 1.0
										else: return 1.4565217391304348
									elif obj[9]>1.0127488151658772:
										# {"feature": "Gender", "instances": 71, "metric_value": 0.0021, "depth": 10}
										if obj[1]>0.0:
											return 2.0
										elif obj[1]<=0.0:
											return 1.0
										else: return 1.411764705882353
									else: return 1.4929577464788732
								elif obj[8]<=1.8070136102120924:
									return 2.0
								else: return 2.0
							elif obj[7]<=4.439355642516821:
								return 1.0
							else: return 1.0
						elif obj[0]<=27.59263559282497:
							# {"feature": "A/G", "instances": 46, "metric_value": 0.0244, "depth": 7}
							if obj[9]<=1.55:
								# {"feature": "TP", "instances": 43, "metric_value": 0.0153, "depth": 8}
								if obj[7]>2.8:
									# {"feature": "ALB", "instances": 42, "metric_value": 0.0219, "depth": 9}
									if obj[8]>3.6214285714285714:
										# {"feature": "Gender", "instances": 26, "metric_value": 0.0051, "depth": 10}
										if obj[1]>0.0:
											return 2.0
										elif obj[1]<=0.0:
											return 2.0
										else: return 1.6666666666666667
									elif obj[8]<=3.6214285714285714:
										# {"feature": "Gender", "instances": 16, "metric_value": 0.0026, "depth": 10}
										if obj[1]>0.0:
											return 2.0
										elif obj[1]<=0.0:
											return 2.0
										else: return 1.75
									else: return 1.8125
								elif obj[7]<=2.8:
									return 1.0
								else: return 1.0
							elif obj[9]>1.55:
								return 2.0
							else: return 2.0
						else: return 1.6521739130434783
					elif obj[5]>68.47035291170018:
						# {"feature": "ALB", "instances": 24, "metric_value": 0.1025, "depth": 6}
						if obj[8]>3.1:
							# {"feature": "Age", "instances": 13, "metric_value": 0.1234, "depth": 7}
							if obj[0]<=39.0:
								# {"feature": "Gender", "instances": 8, "metric_value": 0.0888, "depth": 8}
								if obj[1]>0.0:
									# {"feature": "TP", "instances": 7, "metric_value": 0.0477, "depth": 9}
									if obj[7]>6.3:
										# {"feature": "A/G", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[9]<=0.9:
											return 1.0
										elif obj[9]>0.9:
											return 1.0
										else: return 1.3333333333333333
									elif obj[7]<=6.3:
										return 1.0
									else: return 1.0
								elif obj[1]<=0.0:
									return 2.0
								else: return 2.0
							elif obj[0]>39.0:
								return 1.0
							else: return 1.0
						elif obj[8]<=3.1:
							return 1.0
						else: return 1.0
					else: return 1.125
				elif obj[2]>1.7195653403005178:
					# {"feature": "A/G", "instances": 57, "metric_value": 0.0313, "depth": 5}
					if obj[9]>0.55:
						# {"feature": "Gender", "instances": 50, "metric_value": 0.0309, "depth": 6}
						if obj[1]>0.0:
							# {"feature": "ALB", "instances": 46, "metric_value": 0.0245, "depth": 7}
							if obj[8]>1.4:
								# {"feature": "Age", "instances": 45, "metric_value": 0.0404, "depth": 8}
								if obj[0]<=61.669147898420505:
									# {"feature": "SGPT", "instances": 37, "metric_value": 0.0133, "depth": 9}
									if obj[5]>21.138245436089527:
										# {"feature": "TP", "instances": 35, "metric_value": 0.0297, "depth": 10}
										if obj[7]>5.4:
											return 1.0
										elif obj[7]<=5.4:
											return 1.0
										else: return 1.0
									elif obj[5]<=21.138245436089527:
										return 1.0
									else: return 1.0
								elif obj[0]>61.669147898420505:
									return 1.0
								else: return 1.0
							elif obj[8]<=1.4:
								return 2.0
							else: return 2.0
						elif obj[1]<=0.0:
							return 1.75
						else: return 1.75
					elif obj[9]<=0.55:
						return 1.0
					else: return 1.0
				else: return 1.1929824561403508
			elif obj[4]>726.6886187856755:
				return 1.0
			else: return 1.0
		elif obj[6]>232.0438043817474:
			return 1.0
		else: return 1.0
	elif obj[3]>1.4358369098712498:
		# {"feature": "AP", "instances": 98, "metric_value": 0.065, "depth": 2}
		if obj[4]<=415.8061224489796:
			return 1.0
		elif obj[4]>415.8061224489796:
			# {"feature": "TP", "instances": 30, "metric_value": 0.1247, "depth": 3}
			if obj[7]>6.1:
				return 1.0
			elif obj[7]<=6.1:
				# {"feature": "ALB", "instances": 9, "metric_value": 0.2586, "depth": 4}
				if obj[8]<=2.2:
					return 1.0
				elif obj[8]>2.2:
					return 1.6666666666666667
				else: return 1.6666666666666667
			else: return 1.2222222222222223
		else: return 1.0666666666666667
	else: return 1.0204081632653061
