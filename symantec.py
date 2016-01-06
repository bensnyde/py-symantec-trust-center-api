"""
    Python library for Symantec Trust Center Enterprise API

        https://developers.websecurity.symantec.com/api

    @author     Benton Snyder
    @website    http://bensnyde.me
    @email      benton@bensnyde.me
    @created    1/5/16
    @updated    1/5/16
"""

import requests
import urllib

API_ENDPOINT = 'https://pilot-trustcenter-enterprise.websecurity.symantec.com/service/api/'     # Development
#API_ENDPOINT = 'https://trustcenter-enterprise.websecurity.symantec.com/service/api/'          # Production

class Symantec:
    def __query(self, resource, data):
        url = "%s%s" % (API_ENDPOINT, resource)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = urllib.urlencode(data)

        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 200:
            return r.text
        else:
            r.raise_for_status()

    def enroll_certificate(self, kwargs):
        """
            Enroll for a new certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateEnroll", kwargs)


    def renew_certificate(self, kwargs):
        """
            Renew an expiring or expired certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            usePredecessorSans:     opt str Indicates whether to use SANs from the previous certificate ['True', 'False']
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateRenew", kwargs)

    def replace_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            usePredecessorSans:     opt str Indicates whether to use SANs from the previous certificate ['True', 'False']
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateReplace", data)

    def revoke_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            reason:                 req int Reason for revoking the certificate [1 (key compromise), 2 (affiliation changed) ,3 (superseded) ,4 (cessation of operation)]
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateRevoke", kwargs)


    def pickup_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            format:                 req str Certificate format ['pkcs7', 'x509']
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificatePickup", data)
