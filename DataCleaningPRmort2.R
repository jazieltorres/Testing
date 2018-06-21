library(plyr)
library(tidyr)

AgesDeathCount = AgesDeathCount[-13,]
AgesDeathCount = AgesDeathCount[,-11]
names(AgesDeathCount) = c("Month", "0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+")
AgesDeathCount = gather(AgesDeathCount, Ages, Deaths, -Month)
AgesDeathCount$Month = as.character(rep(1:12, 9))

GenderDeathCount = GenderDeathCount[,-4]
GenderDeathCount = GenderDeathCount[-13,]
names(GenderDeathCount) = c("Month", "F", "M")
GenderDeathCount = gather(GenderDeathCount, Gender, Deaths, -Month)
GenderDeathCount$Month = as.character(rep(1:12, 2))

PlacesDeathCount = PlacesDeathCount[,-8]
PlacesDeathCount = PlacesDeathCount[-13,]
names(PlacesDeathCount) = c("Month", "Emergency Room", "Asylum", "Hospital", "Hospital Arrival","Other", "Residence")
PlacesDeathCount = gather(PlacesDeathCount, PlaceOfDeath, Deaths, -Month)
PlacesDeathCount$Month = as.character(rep(1:12, 6))

CausesDeathCount = CausesDeathCount[,-14]
CausesDeathCount = CausesDeathCount[-41,]
CausesDeathCount$Causa.de.Muerte = c("Tuberculosis","Septicemia","Syphilis","Viral hepatitis","HIV","Malignant neoplasms","Other neoplasms",
                                     "Anemias","Diabetes","Nutritional deficiencies","Meningitis","Parkinson","Alzheimer","Heart disease",
                                     "Hypertensions and hypertensive renal disease","Cerebrovascular disease","Atherosclerosis","Aneurysm",
                                     "Influenza and pneumonia","Bronchitis and bronchiolitis","Chronic lower respiratory diseases","Pneumonitis",
                                     "Peptic ulcer","Diseases of appendix","Hernia","Chronic liver disease and cirrhosis",
                                     "Cholelithiasis and other disorders of gallbladder","Nephritis, nephrotic syndrome and nephrosis",
                                     "Kidney infections","Prostate hyperplasia","Inflammatory diseases of female pelvic organs",
                                     "Pregnancy, childbirth and the puerperium","Certain conditions originating in the perinatal period",
                                     "Congenital malformations, deformations and chromosomal abnormalities","Unintentional injuries","Suicide",
                                     "Homicide","Complications of medical and surgical care","Other","Not specified")
names(CausesDeathCount) = c("DeathCause", as.character(1:12))
CausesDeathCount = gather(CausesDeathCount, Month, Deaths, -DeathCause)
